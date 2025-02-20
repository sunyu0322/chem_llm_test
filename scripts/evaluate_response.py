
def YesOrNo(model_answer: str, true_answer: str) -> dict[str, str]:
    """
    评估模型回答的正确性。
    判断模型的回答是否与真实答案相同，并返回评估结果。
    """
    # 确保 model_answer 和 true_answer 都是字符串，避免调用 strip() 时发生错误
    if isinstance(model_answer, str) and isinstance(true_answer, str):
        is_correct = model_answer.strip() == true_answer.strip()
    else:
        is_correct = "No"  # 如果不是字符串，默认认为答案错误
    
    return {
        "model_answer": model_answer,
        "is_correct": "Yes" if is_correct else "No"
    }