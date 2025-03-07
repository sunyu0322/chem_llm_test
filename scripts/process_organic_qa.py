import os
import re
import csv
from langchain_openai import ChatOpenAI

# 直接集成的模型配置
BASE_URL = "https://api.fe8.cn/v1"
API_KEY = "sk-bsFsOAvTdyNI2MD25vcLXID1vJaYM1hEsN1HMZSuygvXjgiZ"

def generate_answer_from_gpt_4o(query: str) -> str:
    """直接内嵌的模型调用函数"""
    try:
        model = ChatOpenAI(
            model="gpt-4o",
            temperature=0.0,
            base_url=BASE_URL,
            api_key=API_KEY
        )
        response = model.invoke(f'''
        你是一个化学教材解析专家，需要从Markdown内容中提取所有问题对：
        1. 识别所有以"problem"或"question"开头的内容作为问题
        2. 对应的"suggested solution"或"answer"作为答案
        3. 保留所有SMILES代码（格式如`[O]C`）
        4. 按严格CSV格式返回：
           question,answer
           "问题内容","答案内容"
           ...
        以下是需要处理的内容：
        {query}
        ''')
        return response.content.strip()
    
    except Exception as e:
        print(f"模型调用失败: {e}")
        return ""

def process_markdown_file(file_path):
    """处理单个Markdown文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 分批处理（每批最多2048个token）
    batches = [content[i:i+2048] for i in range(0, len(content), 2048)]
    qa_pairs = []
    processed = set()
    
    for batch in batches:
        response = generate_answer_from_gpt_4o(batch)
        if not response:
            continue
        
        # 解析CSV格式响应
        reader = csv.DictReader(response.splitlines())
        for row in reader:
            key = (row['question'], row['answer'])
            if key not in processed:
                qa_pairs.append(row)
                processed.add(key)
    
    return qa_pairs

def main():
    input_dir = "../data_organic_textbook_smiles"
    output_dir = "../QA_organic"
    
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 处理所有Markdown文件
    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            print(f"Processing {filename}")
            file_path = os.path.join(input_dir, filename)
            qa_pairs = process_markdown_file(file_path)
            
            # 保存为CSV
            output_file = os.path.join(output_dir, filename.replace(".md", ".csv"))
            with open(output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=["question", "answer"])
                writer.writeheader()
                writer.writerows(qa_pairs)
            print(f"Saved {len(qa_pairs)} QA pairs to {output_file}")

if __name__ == "__main__":
    main()