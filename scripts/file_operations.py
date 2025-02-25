# file_operations.py
import csv
import os

def write_csv(output_csv_path: str, data: list, fieldnames: list):
    """将数据写入CSV文件"""
    os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
    # 检查文件是否存在，避免写入重复的表头
    file_exists = os.path.exists(output_csv_path)
    with open(output_csv_path, mode='a', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # 仅在文件不存在时写入表头
        if not file_exists:
            writer.writeheader()
        writer.writerows(data)