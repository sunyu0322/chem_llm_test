from langchain_openai import ChatOpenAI

# 大模型配置
BASE_URL = "https://api.fe8.cn/v1"
API_KEY = "sk-pmcyeMITVb2A5keAbnBYbIXpAcyFCROK8jYkIQu4B7E44S3E"

def generate_answer_from_gpt_4o(query: str) -> str:
    """
    使用大模型生成问题的回答。
    该函数通过请求大模型API来生成给定查询的回答。
    """
    try:
        # 初始化 ChatOpenAI 模型
        model = ChatOpenAI(
            model="qwen-max",
            temperature=0,
            base_url=BASE_URL,
            api_key=API_KEY
        )

        # 使用模型生成回答
        response = model.invoke('''
        你是一个化学领域问答助手，根据我给出的问题，进行逻辑推理和思考来完成作答。你的回答应当包括两个部分：
        1. **推理过程**：在这一部分详细描述你的思考过程，包含对相关知识点的分析整理和每一步的逻辑推理，归纳得到能正确回答题目的知识点分析和思考过程。
        2. **答案**：给出最终的答案。若是选择题，请仅输出选择的答案序号（'A', 'B', 'C', 'D'等）；若是填空题，只需要给出填空的答案，不需要解释其他内容。若是简答与计算题，给出完整的解答和计算步骤，条理清晰。
        请注意：不要解释推理过程和答案外的任何额外内容，输出格式必须严格遵循如下：
        **推理过程**：[你的推理过程]
        **答案**：[最终答案]
        ''' + query)
        
        print(f"已获取模型回答: {response.content}")  # 输出模型返回的原始内容
        return response.content.strip()

    except Exception as e:
        print(f"调用大模型时发生错误: {e}")
        return {"error": f"调用失败: {str(e)}"}

def generate_answer_from_gpt_o1(query: str) -> str:
    """
    使用大模型生成问题的回答。
    该函数通过请求大模型API来生成给定查询的回答。
    """
    try:
        # 初始化 ChatOpenAI 模型
        model = ChatOpenAI(
            model="qwen-max",
            temperature=0,
            base_url=BASE_URL,
            api_key=API_KEY
        )

        # 使用模型生成回答
        response = model.invoke('''
        你是一个化学领域问答助手，根据我给出的问题，进行逻辑推理和思考来完成作答。你的回答应当包括两个部分：
        1. **推理过程**：在这一部分详细描述你的思考过程，包含对相关知识点的分析整理和每一步的逻辑推理，归纳得到能正确回答题目的知识点分析和思考过程。
        2. **答案**：给出最终的答案。若是选择题，请仅输出选择的答案序号（'A', 'B', 'C', 'D'等）；若是填空题，只需要给出填空的答案，不需要解释其他内容。若是简答与计算题，给出完整的解答和计算步骤，条理清晰。
        请注意：不要解释推理过程和答案外的任何额外内容，输出格式必须严格遵循如下：
        **推理过程**：[你的推理过程]
        **答案**：[最终答案]
        ''' + query)
        
        print(f"已获取模型回答: {response.content}")  # 输出模型返回的原始内容
        return response.content.strip()

    except Exception as e:
        print(f"调用大模型时发生错误: {e}")
        return {"error": f"调用失败: {str(e)}"}


# model_answer = generate_answer_from_gpt_4o('氢是什么')