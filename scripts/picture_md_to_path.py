import requests
import os
import re

def download_image_from_md(md_tag, output_folder="data_picture"):
    """
    从Markdown图片标签下载图片并保存到本地文件夹。
    """
    # 获取项目根目录并设置为当前工作目录
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(project_root)  # 确保当前工作目录为项目根目录
    print("当前工作目录:", os.getcwd())

    # 生成图片保存的文件夹路径
    output_folder = os.path.join(project_root, output_folder)
    os.makedirs(output_folder, exist_ok=True)

    # 从Markdown标签中提取图片URL
    url_match = re.search(r'src="([^"]+)"', md_tag)
    if not url_match:
        print("❌ 无法从Markdown标签中提取图片URL")
        return None

    image_url = url_match.group(1)
    image_name = os.path.basename(image_url).split("?")[0]  # 去除查询参数
    image_path = os.path.join(output_folder, image_name)

    try:
        # 请求图片并下载
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(image_path, "wb") as f:
                f.write(response.content)
            print(f"✅ 图片已下载到: {image_path}")
            return image_path
        else:
            print(f"❌ 无法下载图片，HTTP状态码: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ 下载图片时出错: {e}")
        return None

# 测试代码
if __name__ == "__main__":
    # 示例Markdown图片标签
    md_tag = '<img src="https://cdn.noedgeai.com/01955a59-12c1-7ea5-a682-05a2b5b6c37d_3.jpg?x=272&y=1394&w=917&h=471&r=0">'

    # 下载图片并打印路径
    image_path = download_image_from_md(md_tag)
    if image_path:
        print(f"📄 图片路径: {image_path}")
