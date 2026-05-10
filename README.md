# 100以内加减法口算题

100以内加减法口算练习项目。

## 项目结构

```
├── README.md
└── tests/
    ├── data/
    │   ├── test_cases.csv          # 测试用例数据
    │   ├── test_questions.txt      # 练习题（无答案）
    │   └── test_answers.txt        # 答案（带完整答案）
    └── program/
        ├── __init__.py
        ├── test_arithmetic_data.py # 数据模块：生成/导入/导出
        └── quiz.py                 # 命令行答题交互
```

## 运行

```bash
# 交互式答题
python3 -m tests.program.quiz
```