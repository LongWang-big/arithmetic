# 100以内加减法口算题

本项目的练习资料用于100以内加减法口算练习。

## 文件说明

```
├── README.md
├── math_quiz.py              # 主程序
├── test_math_quiz.py         # 单元测试
└── results/
    ├── arithmetic_answers.txt    # 练习题（无答案）
    └── arithmetic_questions.txt  # 答案文件（带完整答案）
```

## 运行测试

```bash
python3 -m unittest test_math_quiz -v
```

## 题目规则

- 共50道题
- 包含加法和减法混合运算
- 所有运算结果均在0-100范围内