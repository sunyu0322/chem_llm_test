import csv

def load_csv_data(filename: str) -> list[dict[str, str]]:
    """
    加载CSV数据，返回包含问题和答案的字典列表。
    每行数据应该包含问题（question）和答案（answer）。
    """
    data = []

    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        # 跳过表头，如果有的话
        next(reader)
        
        for row in reader:
            if len(row) < 2:
                # 如果某一行没有足够的列数，跳过该行
                print(f"跳过不完整的行: {row}")
                continue
            
            question = row[0]
            answer = row[1]
            
            # 保存到数据列表中
            data.append({'question': question, 'answer': answer})
    
    return data