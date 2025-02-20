# file_operations.py
import csv
import os

def read_csv(input_csv_path: str):
    """读取CSV文件并返回数据"""
    with open(input_csv_path, mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))

def write_csv(output_csv_path: str, data: list, fieldnames: list):
    """将数据写入CSV文件"""
    os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
    with open(output_csv_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
