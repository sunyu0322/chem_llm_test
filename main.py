import os
from scripts.LLM import generate_answer_from_gpt_4o
from scripts.evaluate_response import YesOrNo
from scripts.load_csv_data import load_csv_data
from scripts.file_operations import read_csv, write_csv

def generate_and_evaluate(input_csv_path: str, output_csv_path: str):
    """
    从CSV文件中获取问题，生成模型回答并进行评估，最后将结果写入输出CSV。
    """
    try:
        # 解析CSV文件，获取问题和答案
        data = load_csv_data(input_csv_path)

        results = []
        for entry in data:
            query = entry.get("question")
            true_answer = entry.get("answer")

            if not query or not true_answer:
                continue  # 跳过缺失问题或答案的记录

            # 生成模型回答
            model_answer = generate_answer_from_gpt_4o(query)

            # 评估模型回答
            eval_result = YesOrNo(model_answer, true_answer)

            # 将评估结果保存
            results.append({
                "query": query,
                "true_answer": true_answer,
                "model_answer": eval_result["model_answer"],
                "is_correct": eval_result["is_correct"]
            })

        # 将结果写入输出CSV
        fieldnames = ["query", "true_answer", "model_answer", "is_correct"]
        write_csv(output_csv_path, results, fieldnames)

        print(f"结果已保存到: {output_csv_path}")

    except Exception as e:
        print(f"发生错误: {e}")

# 调用示例，设置文件路径
if __name__ == "__main__":
    base_dir = "D:/workspace/Gitlab_Projects/chem_llm_test"
    input_csv_path = os.path.join(base_dir, 'Q&A', "原子结构和元素周期律_选择题.csv")  # 修改为你的CSV文件路径
    output_csv_path = os.path.join(base_dir, 'QA_output', "output_原子结构和元素周期律_选择题.csv")  # 修改为输出CSV文件的路径

    generate_and_evaluate(input_csv_path, output_csv_path)
