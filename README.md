

# Chem_llm_test

## 项目简介

该项目的目标是通过使用大语言模型，根据作为 CSV 文件的化学领域问答数据集生成模型回答并进行评估，最后将评估结果保存为新的 CSV 文件。

## 项目结构

```
├── main.py                # 主程序，负责调用生成与评估函数
├── scripts/                # 存放各模块的脚本文件
│   ├── LLM.py             # 生成模型回答的脚本
│   ├── evaluate_response.py # 评估模型回答的脚本
│   ├── load_csv_data.py   # 读取CSV数据的脚本
│   └── file_operations.py # csv文件读写操作
├── /n                   # 存放输入问题和答案的CSV文件
│   └── 原子结构和元素周期律_选择题.csv # 示例输入文件
└── QA_output/             # 存放输出评估结果的CSV文件
    └── output_原子结构和元素周期律_选择题.csv # 示例输出文件
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
