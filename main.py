import os
from scripts.LLM import generate_answer_from_gpt_4o
from scripts.evaluate_response import evaluate_answer_accuracy
from scripts.load_csv_data import load_csv_data
from scripts.file_operations import read_csv, write_csv
from scripts.extract_reasoning_and_answer import extract_reasoning_and_answer  # 引入新的处理函数

def generate_and_evaluate(input_csv_path: str, output_csv_path: str):
    """
    从CSV文件中获取问题，生成模型回答，评估知识准确性、推理准确性和答案的正确性，
    最后将结果写入输出CSV，每处理5条记录保存一次。
    """
    results = []
    try:
        # 解析CSV文件，获取问题和答案
        data = load_csv_data(input_csv_path)
    except Exception as e:
        print(f"解析CSV文件时发生错误: {e}")
        return  # 发生错误时直接返回，避免继续执行

    for idx, entry in enumerate(data):
        query = entry.get("question")
        true_answer = entry.get("answer")

        if not query or not true_answer:
            continue  # 跳过缺失问题或答案的记录

        try:
            # 生成模型回答
            model_answer = generate_answer_from_gpt_4o(query)
        except Exception as e:
            print(f"生成模型回答时发生错误: {e}")
            continue  # 发生错误时跳过当前记录，继续下一个

        try:
            # 提取推理过程和答案
            reasoning_answer = extract_reasoning_and_answer(model_answer)
            if "error" in reasoning_answer:
                print(f"错误处理模型回答: {reasoning_answer['error']}")
                continue  # 发生错误时跳过当前记录，继续下一个
        except Exception as e:
            print(f"提取推理和答案时发生错误: {e}")
            continue  # 发生错误时跳过当前记录，继续下一个

        try:
            # 使用大模型进行知识准确性、推理准确性和最终结果的评估
            eval_result = evaluate_answer_accuracy(reasoning_answer["reasoning"], reasoning_answer["answer"], true_answer)
        except Exception as e:
            print(f"评估模型回答时发生错误: {e}")
            continue  # 发生错误时跳过当前记录，继续下一个

        # 将评估结果保存
        results.append({
            "query": query,
            "true_answer": true_answer,
            "reasoning": reasoning_answer["reasoning"],
            "model_answer": reasoning_answer["answer"],
            "knowledge_accuracy": eval_result.get("knowledge_accuracy", "N/A"),
            "reasoning_accuracy": eval_result.get("reasoning_accuracy", "N/A"),
            "final_answer_accuracy": eval_result.get("final_answer_accuracy", "N/A")
        })

        # 每5条记录保存一次，防止中断时丢失数据
        if (idx + 1) % 5 == 0:
            try:
                fieldnames = ["query", "true_answer", "reasoning", "model_answer", 
                              "knowledge_accuracy", "reasoning_accuracy", "final_answer_accuracy"]
                write_csv(output_csv_path, results, fieldnames)
                print(f"已保存{idx + 1}条数据到: {output_csv_path}")
                results.clear()  # 清空当前结果，防止内存过大
            except Exception as e:
                print(f"写入CSV文件时发生错误: {e}")

    # 最后保存剩余的数据
    if results:
        try:
            fieldnames = ["query", "true_answer", "reasoning", "model_answer", 
                          "knowledge_accuracy", "reasoning_accuracy", "final_answer_accuracy"]
            write_csv(output_csv_path, results, fieldnames)
            print(f"结果已保存到: {output_csv_path}")
        except Exception as e:
            print(f"写入CSV文件时发生错误: {e}")

# 调用示例，设置文件路径
if __name__ == "__main__":
    base_dir = "D:/workspace/Gitlab_Projects/chem_llm_test"
    input_csv_path = os.path.join(base_dir, 'Q&A', "晶体结构_选择题.csv")  # 修改为你的CSV文件路径
    output_csv_path = os.path.join(base_dir, 'QA_output', "晶体结构_选择题_output.csv")  # 修改为输出CSV文件的路径

    generate_and_evaluate(input_csv_path, output_csv_path)
