class Question:
    """封装一道加减法题目的数据及其格式化操作。"""

    def __init__(self, a, op, b, answer):
        self.a = a
        self.op = op
        self.b = b
        self.answer = answer

    def format_question(self):
        return f"{self.a} {self.op} {self.b} = "

    def format_answer(self):
        return f"{self.a} {self.op} {self.b} = {self.answer}"

    def to_numbered_question(self, index):
        return f"{index}. {self.format_question()}"

    def to_numbered_answer(self, index):
        return f"{index}. {self.format_answer()}"
