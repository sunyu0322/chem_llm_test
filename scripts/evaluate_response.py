from langchain_openai import ChatOpenAI

def evaluate_answer_accuracy(reasoning: str, model_answer: str, true_answer: str) -> dict:
    """
    使用大模型来评估模型的回答（知识准确性、推理准确性和最终答案的正确性）。
    返回一个字典，包含每个评估项的得分和详细说明，并在控制台输出评估结果。
    """
    BASE_URL = "https://api.fe8.cn/v1"
    API_KEY = "sk-pmcyeMITVb2A5keAbnBYbIXpAcyFCROK8jYkIQu4B7E44S3E"
    MODEL_NAME = "o1-preview"
    
    try:
        # 初始化 ChatOpenAI 模型
        model = ChatOpenAI(
            model=MODEL_NAME,
            temperature=0,
            base_url=BASE_URL,
            api_key=API_KEY
        )

        # 初始化评估的输入内容
        eval_prompt = f"""
        以下是一个化学问题的回答过程：
        推理过程: {reasoning}
        模型回答: {model_answer}
        真实答案: {true_answer}

        请按照以下步骤进行评估：
        1. 首先，根据标准答案，仔细推理并总结知识点。假设你是一名老师，首先分析并总结标准答案的核心知识和推理过程。
        2. 然后，根据你的分析，结合模型的推理过程和给出的答案，评估其知识准确性、推理准确性和最终答案的正确性：
        
        - **知识准确性**：评估模型的回答是否准确。模型是否正确使用了相关的事实、公式或概念，并且没有出现错误或误解。。
        
        - **推理准确性**：评估模型的推理是否清晰且符合逻辑规则，是否存在推理假设错误或逻辑不严密的情况，检查推理步骤是否有合理的支持和解释，是否能够充分解释为什么得到最终结论。注意，此指标只需检查模型的逻辑是否严密，不需要和你的逻辑完全一致，即使推理路径和你不一样但只要合理即可。
        
        - **最终答案准确性**：评估模型的最终答案是否与真实答案一致。检查模型的最终答案是否直接且完整地回应了问题，是否与标准答案相符。如果标准答案是复杂的，检查模型的回答是否遗漏了任何重要部分。

        3. 请为每项评分给出0到1之间的小数，避免极端值（0或1），并根据每项内容的合理性给予扣分。若最终答案完全一致，则评分为1。

        输出格式：
        知识准确性：[准确性评分，0到1之间的小数]
        推理准确性：[推理准确性评分，0到1之间的小数]
        最终答案准确性：[答案准确性评分，0到1之间的小数]
        
        **请严格按照输出格式回答，不要输出任何其他内容。**
        """

        # 调用大模型进行评估
        eval_response = model.invoke(eval_prompt)
        eval_result = eval_response.content.strip()

        # 初始化评分字典
        scores = {}
        # 按行分割结果
        for line in eval_result.split("\n"):
            # 获取知识准确性
            if line.startswith("知识准确性"):
                accuracy = line.split("：")[1].strip()
                accuracy = accuracy.strip("[]")  # 去除方括号
                scores["knowledge_accuracy"] = float(accuracy) if accuracy else "N/A"
            # 获取推理准确性
            elif line.startswith("推理准确性"):
                accuracy = line.split("：")[1].strip()
                accuracy = accuracy.strip("[]")  # 去除方括号
                scores["reasoning_accuracy"] = float(accuracy) if accuracy else "N/A"
            # 获取最终答案准确性
            elif line.startswith("最终答案准确性"):
                accuracy = line.split("：")[1].strip()
                accuracy = accuracy.strip("[]")  # 去除方括号
                scores["final_answer_accuracy"] = float(accuracy) if accuracy else "N/A"

        # 打印评估结果
        print(f"评估结果：")
        print(f"知识准确性：{scores.get('knowledge_accuracy', 'N/A')}")
        print(f"推理准确性：{scores.get('reasoning_accuracy', 'N/A')}")
        print(f"最终答案准确性：{scores.get('final_answer_accuracy', 'N/A')}")
        print("------")  # 用于分隔不同条目的结果
        
        # 返回评估结果
        return scores

    except Exception as e:
        print(f"评估过程中发生错误: {e}")
        return {"error": f"评估失败: {str(e)}"}

def evaluate_none(reasoning: str, model_answer: str, true_answer: str) -> dict:
    """
    不通过任何大模型评估，仅生成NA占位结果。
    返回格式与真实评估函数完全一致的字典，并在控制台输出NA结果。
    """
    # 直接构造NA结果
    scores = {
        "knowledge_accuracy": "N/A",
        "reasoning_accuracy": "N/A",
        "final_answer_accuracy": "N/A"
    }
    
    return scores