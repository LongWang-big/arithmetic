import unittest
from math_quiz import generate_quiz


class TestMathQuiz(unittest.TestCase):

    def test_generate_quiz_default_count(self):
        """测试默认生成100道题"""
        questions = generate_quiz()
        self.assertEqual(len(questions), 100)

    def test_generate_quiz_custom_count(self):
        """测试自定义题目数量"""
        questions = generate_quiz(50)
        self.assertEqual(len(questions), 50)

        questions = generate_quiz(10)
        self.assertEqual(len(questions), 10)

    def test_question_format(self):
        """测试题目格式为(a, op, b, answer)"""
        questions = generate_quiz(10)
        for q in questions:
            self.assertEqual(len(q), 4)
            a, op, b, answer = q
            self.assertIsInstance(a, int)
            self.assertIn(op, ['+', '-'])
            self.assertIsInstance(b, int)
            self.assertIsInstance(answer, int)

    def test_number_range(self):
        """测试数字范围：a在1-100，b根据运算符有不同范围"""
        questions = generate_quiz(100)
        for a, op, b, answer in questions:
            self.assertGreaterEqual(a, 1)
            self.assertLessEqual(a, 100)
            if op == '+':
                self.assertGreaterEqual(b, 1)
            else:  # 减法时b可以为0
                self.assertGreaterEqual(b, 0)
            self.assertLessEqual(b, 100)

    def test_subtraction_result_non_negative(self):
        """测试减法结果非负"""
        questions = generate_quiz(100)
        for a, op, b, answer in questions:
            if op == '-':
                self.assertGreaterEqual(a, b, f"减法时被减数应大于等于减数: {a} - {b}")
                self.assertGreaterEqual(answer, 0)

    def test_answer_correctness(self):
        """测试答案计算正确"""
        questions = generate_quiz(100)
        for a, op, b, answer in questions:
            if op == '+':
                expected = a + b
            else:
                expected = a - b
            self.assertEqual(answer, expected, f"{a} {op} {b} 的答案应为 {expected}，实际为 {answer}")

    def test_result_within_100(self):
        """测试加法结果不超过100"""
        questions = generate_quiz(100)
        for a, op, b, answer in questions:
            if op == '+':
                self.assertLessEqual(answer, 100, f"{a} + {b} = {answer} 超过100")


if __name__ == '__main__':
    unittest.main()