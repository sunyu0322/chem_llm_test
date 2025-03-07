

# Chem_llm_test

## 项目简介

该项目的目标是通过使用大语言模型，根据作为 CSV 文件的化学领域问答数据集生成模型回答并进行评估，最后将评估结果保存为新的 CSV 文件。

## 项目结构

```


chem_llm/
├── data_organic_textbook/                # 原始有机化学教材Markdown文件
│   ├── clayden_question.md               # 示例文件
├── data_organic_textbook_smiles/         # 处理后的Markdown文件（图片替换为SMILES）
│   ├── clayden_question_smiles.md        # 示例输出文件
├── data_picture/                         # 临时下载的图片
│   └── 01955a59-12c1-7ea5-a682-05a2b5b6c37d...  # 示例图片
├── Q&A_inorganic/                        # 无机化学问答对
├── QA_output/                            # 临时输出文件
├── QA_output_inorganic/                  # 无机化学相关输出文件
├── scripts/                              # 脚本目录
│   ├── evaluate_response.py              # 评估模型回答的脚本
│   ├── extract_reasoning_and_answer.py   # 提取推理和答案脚本
│   ├── file_operations.py                # csv文件操作脚本
│   ├── jpg_to_smiles.py                  # 图片转SMILES脚本
│   ├── LLM.py                            # 大模型相关脚本
│   ├── load_csv_data.py                  # 加载CSV数据脚本
│   ├── picture_md_to_path.py             # Markdown图片转路径脚本
│   └── process_organic_textbook.py       # 处理有机化学教材脚本
├── main.py                # 主程序，负责调用生成与评估函数
```

## 安装依赖

请确保已经安装以下依赖：



```bash

```

## 使用说明

### 1. 修改文件路径

在 `main.py` 中，你需要设置输入和输出的文件路径。

```python
if __name__ == "__main__":
    base_dir = "D:/workspace/Gitlab_Projects/chem_llm_test"
    input_csv_path = os.path.join(base_dir, 'Q&A', "原子结构和元素周期律_选择题.csv")  # 修改为你的CSV文件路径
    output_csv_path = os.path.join(base_dir, 'QA_output', "output_原子结构和元素周期律_选择题.csv")  # 修改为输出CSV文件的路径

    generate_and_evaluate(input_csv_path, output_csv_path)
```

- **input_csv_path**：输入文件的路径，包含问题和答案。
- **output_csv_path**：生成的评估结果文件路径。

### 2. 运行程序

运行 `main.py` 脚本，如：

```bash
python main.py
```

程序会从指定的输入文件中读取问题和答案，生成模型的回答，并与真实答案进行对比，最终将评估结果输出到指定的输出文件中。

### 3. 输出文件

评估结果会保存在指定的 CSV 文件中，格式如下：

```
query, true_answer, model_answer, is_correct(后续会改为其他评估指标)
问题1, 答案1, 模型回答1, 是否正确(后续会改为其他评估指标)
问题2, 答案2, 模型回答2, 是否正确(后续会改为其他评估指标)
...
```

---
### picture_md_to_path.py

该脚本用于从Markdown图片标签中提取图片URL，下载图片到 `data_picture` 文件夹，并调用DECIMER生成SMILES。
<!-- 
## 使用方法
1. 将Markdown图片标签作为输入。
2. 运行脚本：
   ```bash
   python picture_md_to_path.py -->