import csv
import os
import random

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")


def generate_question():
    """生成一道100以内加减法题，返回 (a, op, b, answer)"""
    op = random.choice(['+', '-'])
    if op == '+':
        a = random.randint(1, 99)
        b = random.randint(1, 100 - a)
    else:
        a = random.randint(1, 100)
        b = random.randint(0, a)
    answer = a + b if op == '+' else a - b
    return (a, op, b, answer)


def generate_quiz(num_questions=100):
    """生成指定数量的题目"""
    return [generate_question() for _ in range(num_questions)]


def format_question(a, op, b, answer=None):
    """格式化题目，带答案或不带答案"""
    if answer is not None:
        return f"{a} {op} {b} = {answer}"
    return f"{a} {op} {b} = "


def save_questions(questions, question_path, answer_path):
    """将题目和答案分别保存到文件"""
    question_lines = []
    answer_lines = []

    for i, (a, op, b, answer) in enumerate(questions, 1):
        question_lines.append(f"{i}. {format_question(a, op, b)}")
        answer_lines.append(f"{i}. {format_question(a, op, b, answer)}")

    with open(question_path, 'w') as f:
        f.write('\n'.join(question_lines))

    with open(answer_path, 'w') as f:
        f.write('\n'.join(answer_lines))


def load_cases(csv_path=None):
    """从CSV文件加载测试用例"""
    if csv_path is None:
        csv_path = os.path.join(DATA_DIR, "test_cases.csv")
    cases = []
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            a = int(row['a'])
            op = row['op']
            b = int(row['b'])
            answer = int(row['answer'])
            cases.append((a, op, b, answer))
    return cases


def export_quiz(num_questions=50):
    """生成题目并导出到 data 目录"""
    questions = generate_quiz(num_questions)
    q_path = os.path.join(DATA_DIR, "test_questions.txt")
    a_path = os.path.join(DATA_DIR, "test_answers.txt")
    save_questions(questions, q_path, a_path)
    return questions
