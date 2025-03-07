import os
from DECIMER import predict_SMILES

def image_to_smiles(image_path):
    """
    从本地图片生成SMILES。
    """
    try:
        SMILES = predict_SMILES(image_path)
        print(f"🎉 Decoded SMILES: {SMILES}")  # 在函数内部打印结果
        return SMILES
    except Exception as e:
        print(f"❌ 生成SMILES时出错: {e}")
        # 打印更详细的错误信息
        import traceback
        traceback.print_exc()
        return None

# 测试代码
if __name__ == "__main__":
    # 设置当前工作目录为项目根目录
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(project_root)  # 确保当前工作目录为项目根目录
    print("当前工作目录:", os.getcwd())

    # 示例图片路径（假设图片已下载到 data_picture 文件夹）
    image_path = "data_picture/01955a59-12c1-7ea5-a682-05a2b5b6c37d_3.jpg"

    # 生成SMILES并打印
    SMILES = image_to_smiles(image_path)

