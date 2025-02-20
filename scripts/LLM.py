from langchain_openai import ChatOpenAI


# 大模型配置
BASE_URL = "https://api.fe8.cn/v1"
API_KEY = "sk-pmcyeMITVb2A5keAbnBYbIXpAcyFCROK8jYkIQu4B7E44S3E"
MODEL_NAME = "gpt-4o"

def generate_answer_from_gpt_4o(query: str) -> str:
    """
    使用大模型生成问题的回答。
    该函数通过请求大模型API来生成给定查询的回答。
    """
    BASE_URL = "https://api.fe8.cn/v1"
    API_KEY = "sk-pmcyeMITVb2A5keAbnBYbIXpAcyFCROK8jYkIQu4B7E44S3E"
    MODEL_NAME = "gpt-4o"
    try:
        # 初始化 ChatOpenAI 模型
        model = ChatOpenAI(
            model=MODEL_NAME,
            temperature=0,
            base_url=BASE_URL,
            api_key=API_KEY
        )

        # 使用模型生成回答
        response = model.invoke(query)
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

        # 使用模型生成回答
        response = model.invoke(query)
        print(f"已获取模型回答: {response.content}")  # 输出模型返回的原始内容
        return response.content.strip()

    except Exception as e:
        print(f"调用大模型时发生错误: {e}")
        return {"error": f"调用失败: {str(e)}"}
