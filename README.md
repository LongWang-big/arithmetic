# 100以内加减法口算题

本项目的练习资料用于100以内加减法口算练习。

## 项目结构

```
├── README.md
└── tests/
    ├── data/
    │   ├── arithmetic_answers.txt    # 练习题（无答案）
    │   └── arithmetic_questions.txt  # 答案（带完整答案）
    └── program/
        ├── __init__.py
        ├── math_quiz.py              # 主程序
        └── test_math_quiz.py         # 单元测试
```

## 运行测试

```bash
python3 -m tests.program.test_math_quiz -v
```

## 运行答题程序

```bash
python3 -m tests.program.math_quiz
```