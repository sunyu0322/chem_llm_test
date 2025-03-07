# scripts/process_organic_textbook.py
import os
import re
import sys
import requests
from bs4 import BeautifulSoup
from picture_md_to_path import download_image_from_md
from jpg_to_smiles import image_to_smiles

# ======================
# 工具函数
# ======================
def is_valid_img_tag(tag):
    """使用HTML解析器验证标签完整性"""
    try:
        soup = BeautifulSoup(tag, 'html.parser')
        img = soup.find('img')
        return bool(img and img.get('src'))
    except Exception:
        return False

def safe_write(content, output_path):
    """原子写入防止数据损坏"""
    temp_path = output_path + ".tmp"
    with open(temp_path, "w", encoding="utf-8") as f:
        f.write(content)
    if os.path.exists(output_path):
        os.remove(output_path)
    os.rename(temp_path, output_path)

# ======================
# 核心处理逻辑
# ======================
def process_md_file(input_md_path, output_md_path):
    # 进度跟踪初始化
    progress_file = output_md_path + ".progress"
    processed_urls = set()
    if os.path.exists(progress_file):
        with open(progress_file, "r") as f:
            processed_urls = set(f.read().splitlines())
        print(f"🔍 检测到未完成进度，已跳过 {len(processed_urls)} 个图片")

    # 读取原始内容
    with open(input_md_path, "r", encoding="utf-8") as f:
        original_content = f.read()
    
    # 准备正则表达式（严格模式）
    img_pattern = re.compile(
        r'<img\s+src="([^"]+)"'  # 匹配src属性
        r'(?:\s+[a-zA-Z-]+="[^"]*")*'  # 允许其他属性
        r'\s*/?>',  # 支持自闭合标签
        flags=re.IGNORECASE
    )
    matches = list(img_pattern.finditer(original_content))
    total = len(matches)

    try:
        content_list = list(original_content)
        for idx, match in enumerate(matches, 1):
            full_tag = match.group(0)
            image_url = match.group(1)
            
            # 跳过已处理
            if image_url in processed_urls:
                print(f"⏩ 跳过已处理 ({idx}/{total}): {image_url[:30]}...")
                continue
                
            # 标签完整性验证
            if not is_valid_img_tag(full_tag):
                print(f"⚠️ 忽略无效标签: {full_tag[:50]}...")
                continue
                
            print(f"🔄 处理中 ({idx}/{total}): {image_url[:30]}...")

            # 下载转换流程
            try:
                image_path = download_image_from_md(
                    f'<img src="{image_url}">', 
                    output_folder="data_picture"
                )
                if not (image_path and os.path.exists(image_path)):
                    raise FileNotFoundError("图片下载失败")
                    
                smiles = image_to_smiles(image_path)
                if not smiles:
                    raise ValueError("SMILES生成失败")
                    
                # 执行替换
                start, end = match.start(), match.end()
                content_list[start:end] = f'`{smiles}`'
                
                # 更新进度
                with open(progress_file, "a") as f:
                    f.write(f"{image_url}\n")
                safe_write("".join(content_list), output_md_path)
                
            except Exception as e:
                print(f"❌ 处理失败: {str(e)}")
                continue

        # 清理进度文件
        if os.path.exists(progress_file):
            os.remove(progress_file)
        print(f"✅ 处理完成: {output_md_path}")

    except KeyboardInterrupt:
        print("\n⚠️ 捕获中断信号！正在保存当前进度...")
        safe_write("".join(content_list), output_md_path)
        print(f"⏸️ 已保存当前状态到: {output_md_path}")
        print(f"🔧 下次运行将自动继续")
        sys.exit(1)

# ======================
# 主程序入口
# ======================
if __name__ == "__main__":
    # 输入输出路径配置
    input_md = "data_organic_textbook/基础有机化学习题解析.md"
    output_md = "data_organic_textbook_smiles/基础有机化学习题解析_smiles.md"
    
    # 初始化环境
    os.makedirs(os.path.dirname(output_md), exist_ok=True)
    
    # 执行处理流程
    process_md_file(input_md, output_md)