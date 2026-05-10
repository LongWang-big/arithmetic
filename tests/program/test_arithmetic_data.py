import os
import unittest
import tempfile

from program.formatter import (
    format_answer,
    format_numbered_answers,
    format_numbered_questions,
    format_question,
)
from program.question_generator import generate_question, generate_quiz
from program.storage import append_quiz, load_cases

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")


class TestArithmeticData(unittest.TestCase):

    def test_generate_question_structure(self):
        a, op, b, answer = generate_question()
        self.assertIn(op, ('+', '-'))
        self.assertIsInstance(a, int)
        self.assertIsInstance(b, int)
        self.assertIsInstance(answer, int)

    def test_generate_question_result_range(self):
        for _ in range(500):
            a, op, b, answer = generate_question()
            self.assertGreaterEqual(answer, 0)
            self.assertLessEqual(answer, 100)

    def test_generate_question_addition_correct(self):
        for _ in range(200):
            a, op, b, answer = generate_question()
            if op == '+':
                self.assertEqual(answer, a + b)

    def test_generate_question_subtraction_correct(self):
        for _ in range(200):
            a, op, b, answer = generate_question()
            if op == '-':
                self.assertEqual(answer, a - b)
                self.assertGreaterEqual(a, b)

    def test_generate_question_addition_b_not_exceed_limit(self):
        for _ in range(200):
            a, op, b, answer = generate_question()
            if op == '+':
                self.assertLessEqual(answer, 100)

    def test_generate_quiz_count(self):
        self.assertEqual(len(generate_quiz(10)), 10)
        self.assertEqual(len(generate_quiz(50)), 50)
        self.assertEqual(len(generate_quiz(100)), 100)

    def test_format_question(self):
        self.assertEqual(format_question(3, '+', 5), "3 + 5 = ")
        self.assertEqual(format_question(10, '-', 3), "10 - 3 = ")

    def test_format_answer(self):
        self.assertEqual(format_answer(3, '+', 5, 8), "3 + 5 = 8")
        self.assertEqual(format_answer(10, '-', 3, 7), "10 - 3 = 7")

    def test_append_quiz(self):
        questions = [(1, '+', 2, 3)]
        with tempfile.TemporaryDirectory() as tmpdir:
            q_path = os.path.join(tmpdir, "q.txt")
            a_path = os.path.join(tmpdir, "a.txt")
            append_quiz(questions, q_path, a_path)

            with open(q_path, encoding='utf-8') as f:
                self.assertEqual(f.read().rstrip('\n'), "1. 1 + 2 = ")

            with open(a_path, encoding='utf-8') as f:
                self.assertEqual(f.read().rstrip('\n'), "1. 1 + 2 = 3")

            append_quiz([(4, '-', 1, 3)], q_path, a_path)
            with open(q_path, encoding='utf-8') as f:
                self.assertEqual(
                    f.read().rstrip('\n'),
                    "1. 1 + 2 = \n1. 4 - 1 = ",
                )

    def test_load_cases(self):
        cases = load_cases(os.path.join(DATA_DIR, "test_cases.csv"))
        self.assertGreater(len(cases), 0)
        for a, op, b, answer in cases:
            self.assertIn(op, ('+', '-'))
            if op == '+':
                self.assertEqual(answer, a + b)
            else:
                self.assertEqual(answer, a - b)

    def test_fixture_text_matches_csv(self):
        """tests/data 中题目、答案文本与 test_cases.csv 一致。"""
        cases = load_cases(os.path.join(DATA_DIR, "test_cases.csv"))
        expect_q = '\n'.join(format_numbered_questions(cases)) + '\n'
        expect_a = '\n'.join(format_numbered_answers(cases)) + '\n'
        q_path = os.path.join(DATA_DIR, "test_questions.txt")
        a_path = os.path.join(DATA_DIR, "test_answers.txt")
        with open(q_path, encoding='utf-8') as f:
            self.assertEqual(f.read(), expect_q)
        with open(a_path, encoding='utf-8') as f:
            self.assertEqual(f.read(), expect_a)


if __name__ == '__main__':
    unittest.main()
