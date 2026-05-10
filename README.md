# 100以内加减法口算题

100以内加减法口算练习项目，采用模块化设计。

## 项目结构

```
├── README.md
└── tests/
    ├── data/
    │   ├── arithmetic_answers.txt    # 练习题（无答案）
    │   └── arithmetic_questions.txt  # 答案（带完整答案）
    └── program/
        ├── __init__.py
        ├── generator.py              # 题目生成
        ├── quiz.py                   # 答题交互
        ├── file_handler.py           # 文件读写
        ├── main.py                   # 主入口
        └── test_math_quiz.py         # 单元测试
```

## 模块说明

| 模块 | 职责 |
|------|------|
| `generator.py` | 生成题目和算式，确保结果在100以内 |
| `quiz.py` | 命令行交互式答题 |
| `file_handler.py` | 题目/答案格式化与文件读写 |
| `main.py` | 主入口：生成题目并导出到文件 |

## 运行

```bash
# 运行测试
python3 -m tests.program.test_math_quiz -v

# 导出题目到文件
python3 -m tests.program.main

# 交互式答题
python3 -m tests.program.quiz
```