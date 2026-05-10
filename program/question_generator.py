import random

from program import config


def generate_question():
    """生成一道 MAX_ANSWER 以内加减法题，返回 (a, op, b, answer)"""
    cap = config.MAX_ANSWER
    op = random.choice(['+', '-'])
    if op == '+':
        a = random.randint(1, cap - 1)
        b = random.randint(1, min(cap - a, cap - 1))
    else:
        a = random.randint(1, cap)
        b = random.randint(0, a)
    answer = a + b if op == '+' else a - b
    return a, op, b, answer


def generate_quiz(num=None):
    n = num if num is not None else config.QUESTION_COUNT
    return [generate_question() for _ in range(n)]
