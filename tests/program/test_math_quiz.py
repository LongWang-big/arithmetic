import unittest
import os
import tempfile
from .generator import generate_question, generate_quiz
from .file_handler import format_question, save_questions


class TestGenerator(unittest.TestCase):

    def test_generate_question_format(self):
        """测试单题格式"""
        a, op, b, answer = generate_question()
        self.assertIsInstance(a, int)
        self.assertIn(op, ['+', '-'])
        self.assertIsInstance(b, int)
        self.assertIsInstance(answer, int)

    def test_generate_question_addition(self):
        """测试加法结果在100以内"""
        for _ in range(200):
            a, op, b, answer = generate_question()
            if op == '-':
                continue
            self.assertGreaterEqual(a, 1)
            self.assertGreaterEqual(b, 1)
            self.assertGreaterEqual(answer, 2)
            self.assertLessEqual(answer, 100)

    def test_generate_question_subtraction(self):
        """测试减法结果非负"""
        for _ in range(200):
            a, op, b, answer = generate_question()
            if op == '+':
                continue
            self.assertGreaterEqual(a, b)
            self.assertGreaterEqual(answer, 0)

    def test_generate_quiz_default_count(self):
        """测试默认生成100道题"""
        self.assertEqual(len(generate_quiz()), 100)

    def test_generate_quiz_custom_count(self):
        """测试自定义题目数量"""
        self.assertEqual(len(generate_quiz(50)), 50)
        self.assertEqual(len(generate_quiz(10)), 10)

    def test_quiz_answers_correctness(self):
        """测试所有题目答案计算正确"""
        for a, op, b, answer in generate_quiz(100):
            expected = a + b if op == '+' else a - b
            self.assertEqual(answer, expected)


class TestFileHandler(unittest.TestCase):

    def test_format_question_without_answer(self):
        """测试不带答案的格式化"""
        result = format_question(3, '+', 5)
        self.assertEqual(result, "3 + 5 = ")

    def test_format_question_with_answer(self):
        """测试带答案的格式化"""
        result = format_question(3, '+', 5, 8)
        self.assertEqual(result, "3 + 5 = 8")

    def test_save_questions(self):
        """测试保存题目和答案到文件"""
        questions = [(1, '+', 2, 3), (5, '-', 3, 2)]

        with tempfile.TemporaryDirectory() as tmpdir:
            q_path = os.path.join(tmpdir, "questions.txt")
            a_path = os.path.join(tmpdir, "answers.txt")
            save_questions(questions, q_path, a_path)

            with open(q_path) as f:
                questions_content = f.read().strip()
            with open(a_path) as f:
                answers_content = f.read().strip()

            self.assertEqual(questions_content, "1. 1 + 2 = \n2. 5 - 3 =")
            self.assertEqual(answers_content, "1. 1 + 2 = 3\n2. 5 - 3 = 2")


class TestMain(unittest.TestCase):

    def test_main_generates_files(self):
        """测试主入口生成文件"""
        from .main import main
        with tempfile.TemporaryDirectory() as tmpdir:
            import tests.program.main as m
            m.QUESTION_PATH = os.path.join(tmpdir, "q.txt")
            m.ANSWER_PATH = os.path.join(tmpdir, "a.txt")
            main()
            self.assertTrue(os.path.exists(m.QUESTION_PATH))
            self.assertTrue(os.path.exists(m.ANSWER_PATH))


if __name__ == '__main__':
    unittest.main()
