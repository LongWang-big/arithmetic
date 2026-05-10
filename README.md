# 100以内加减法口算题

100以内加减法口算练习项目。

## 项目结构

```
├── README.md
├── program/
│   ├── __init__.py
│   ├── config.py                 # 题目数量、结果上限、结果目录等配置
│   ├── question_generator.py     # 随机加法 / 减法题
│   ├── formatter.py              # 题目与答案的文本格式
│   ├── storage.py                # 文本追加写入文件；CSV 用例加载
│   └── arithmetic_practice.py    # 程序入口：生成、展示、保存
├── results/
│   ├── arithmetic_questions.txt  # 口算题（无答案，多次运行会追加）
│   └── arithmetic_answers.txt    # 完整算式答案（追加）
└── tests/
    ├── data/
    │   ├── test_cases.csv        # 用例：a, op, b, 期望答案
    │   ├── test_questions.txt    # 与 CSV 对应的预期题目文本
    │   └── test_answers.txt      # 与 CSV 对应的预期答案文本
    └── program/
        └── test_arithmetic_data.py  # 校验运算、范围及 fixtures 与 CSV 一致
```

### tests/data 文件说明

| 文件 | 放什么 | 用途 |
|------|--------|------|
| `test_cases.csv` | 左操作数、运算符、右操作数、期望答案 | 结构化单元测试数据源 |
| `test_questions.txt` | 与 CSV 行一致的题目文本 | 与 `formatter` 输出对照 |
| `test_answers.txt` | 与 CSV 行一致的答案文本 | 与 `formatter` 输出对照 |

修改 `test_cases.csv` 后，需按相同顺序更新两个 `.txt`（或从 CSV 用 `formatter` 重新生成），否则 `test_fixture_text_matches_csv` 会失败。

## 运行

```bash
# 在项目根目录：生成题目、终端展示、追加写入 results/
python3 -m program.arithmetic_practice

# 运行单元测试
python3 -m unittest tests.program.test_arithmetic_data -v
```

## 测试

单元测试覆盖：出题结构与范围（0～100）、加减正确性、格式化、`append_quiz` 追加写入、CSV 加载与验算、`test_questions.txt` / `test_answers.txt` 与 `test_cases.csv` 一致性。
