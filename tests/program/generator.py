import random


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
