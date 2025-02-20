def extract_reasoning_and_answer(model_response: str) -> dict:
    """
    从大模型返回的回答中提取推理过程和答案。
    通过简单的字符串操作，不使用正则表达式。
    """
    try:
        # 查找 "推理过程" 和 "答案" 的位置
        reasoning_start = model_response.find("**推理过程**")
        answer_start = model_response.find("**答案**")  # 修改这里，去掉多余的冒号

        if reasoning_start == -1 or answer_start == -1:
            return {"error": "推理过程或答案部分缺失"}

        # 提取推理过程和答案
        reasoning_text = model_response[reasoning_start + len("**推理过程**"):answer_start].strip()
        answer_text = model_response[answer_start + len("**答案**"):].strip()

        return {"reasoning": reasoning_text, "answer": answer_text}

    except Exception as e:
        return {"error": f"处理模型回答时发生错误: {str(e)}"}
    