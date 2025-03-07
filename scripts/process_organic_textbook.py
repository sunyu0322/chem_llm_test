# scripts/process_organic_textbook.py
import os
import re
from picture_md_to_path import download_image_from_md
from jpg_to_smiles import image_to_smiles

def process_md_file(input_md_path, output_md_path):
    """
    处理Markdown文件，实时保存处理结果
    """
    # 确保输出目录存在
    os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
    
    try:
        # 读取原始内容
        with open(input_md_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"读取输入文件失败: {e}")
        return

    # 查找所有图片标签
    img_pattern = re.compile(r'<img\s+src="([^"]+)"[^>]*>')
    matches = list(img_pattern.finditer(content))  # 转换为列表以便反向遍历

    # 反向处理避免位置偏移
    for match in reversed(matches):
        try:
            image_url = match.group(1)
            # 下载图片
            image_path = download_image_from_md(f'<img src="{image_url}">', output_folder="data_picture")
            
            if not (image_path and os.path.exists(image_path)):
                continue
                
            # 生成SMILES
            smiles = image_to_smiles(image_path)
            if not smiles:
                continue
                
            # 更新内容
            start, end = match.span()
            new_content = content[:start] + f'`{smiles}`' + content[end:]
            
            # 实时保存
            with open(output_md_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            # 更新内存中的内容
            content = new_content
                
        except Exception as e:
            print(f"处理图片 {image_url} 时出错: {str(e)}")
            continue

    print(f"✅ 最终文件已保存到: {output_md_path}")

if __name__ == "__main__":
    input_md = "data_organic_textbook/基础有机化学习题解析.md"
    output_md = "data_organic_textbook_smiles/基础有机化学习题解析_smiles.md"
    
    process_md_file(input_md, output_md)