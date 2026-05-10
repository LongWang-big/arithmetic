import random

from program.question import Question


class QuestionGenerator:
    """封装题目生成逻辑与配置。"""

    def __init__(self, max_answer=100, question_count=50):
        self.max_answer = max_answer
        self.question_count = question_count

    def generate_one(self):
        cap = self.max_answer
        op = random.choice(['+', '-'])
        if op == '+':
            a = random.randint(1, cap - 1)
            b = random.randint(1, min(cap - a, cap - 1))
        else:
            a = random.randint(1, cap)
            b = random.randint(0, a)
        answer = a + b if op == '+' else a - b
        return Question(a, op, b, answer)

    def generate_quiz(self, count=None):
        n = count if count is not None else self.question_count
        return [self.generate_one() for _ in range(n)]
