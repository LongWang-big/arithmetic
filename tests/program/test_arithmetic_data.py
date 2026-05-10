import os
import unittest
import tempfile

from program.question import Question
from program.question_generator import QuestionGenerator
from program.storage import QuizFileHandler

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")


class TestArithmeticData(unittest.TestCase):

    def setUp(self):
        self.generator = QuestionGenerator(max_answer=100)
        self.handler = QuizFileHandler()

    def test_generate_question_structure(self):
        q = self.generator.generate_one()
        self.assertIn(q.op, ('+', '-'))
        self.assertIsInstance(q.a, int)
        self.assertIsInstance(q.b, int)
        self.assertIsInstance(q.answer, int)

    def test_generate_question_result_range(self):
        for _ in range(500):
            q = self.generator.generate_one()
            self.assertGreaterEqual(q.answer, 0)
            self.assertLessEqual(q.answer, 100)

    def test_generate_question_addition_correct(self):
        for _ in range(200):
            q = self.generator.generate_one()
            if q.op == '+':
                self.assertEqual(q.answer, q.a + q.b)

    def test_generate_question_subtraction_correct(self):
        for _ in range(200):
            q = self.generator.generate_one()
            if q.op == '-':
                self.assertEqual(q.answer, q.a - q.b)
                self.assertGreaterEqual(q.a, q.b)

    def test_generate_question_addition_b_not_exceed_limit(self):
        for _ in range(200):
            q = self.generator.generate_one()
            if q.op == '+':
                self.assertLessEqual(q.answer, 100)

    def test_generate_quiz_count(self):
        self.assertEqual(len(self.generator.generate_quiz(10)), 10)
        self.assertEqual(len(self.generator.generate_quiz(50)), 50)
        self.assertEqual(len(self.generator.generate_quiz(100)), 100)

    def test_format_question(self):
        q = Question(3, '+', 5, 8)
        self.assertEqual(q.format_question(), "3 + 5 = ")
        q2 = Question(10, '-', 3, 7)
        self.assertEqual(q2.format_question(), "10 - 3 = ")

    def test_format_answer(self):
        q = Question(3, '+', 5, 8)
        self.assertEqual(q.format_answer(), "3 + 5 = 8")
        q2 = Question(10, '-', 3, 7)
        self.assertEqual(q2.format_answer(), "10 - 3 = 7")

    def test_append_quiz(self):
        questions = [Question(1, '+', 2, 3)]
        with tempfile.TemporaryDirectory() as tmpdir:
            q_path = os.path.join(tmpdir, "q.txt")
            a_path = os.path.join(tmpdir, "a.txt")
            self.handler.append_quiz(questions, q_path, a_path)

            with open(q_path, encoding='utf-8') as f:
                self.assertEqual(f.read().rstrip('\n'), "1. 1 + 2 = ")

            with open(a_path, encoding='utf-8') as f:
                self.assertEqual(f.read().rstrip('\n'), "1. 1 + 2 = 3")

            self.handler.append_quiz([Question(4, '-', 1, 3)], q_path, a_path)
            with open(q_path, encoding='utf-8') as f:
                self.assertEqual(
                    f.read().rstrip('\n'),
                    "1. 1 + 2 = \n1. 4 - 1 = ",
                )

    def test_load_cases(self):
        cases = self.handler.load_cases(os.path.join(DATA_DIR, "test_cases.csv"))
        self.assertGreater(len(cases), 0)
        for q in cases:
            self.assertIn(q.op, ('+', '-'))
            if q.op == '+':
                self.assertEqual(q.answer, q.a + q.b)
            else:
                self.assertEqual(q.answer, q.a - q.b)

    def test_fixture_text_matches_csv(self):
        cases = self.handler.load_cases(os.path.join(DATA_DIR, "test_cases.csv"))
        expect_q = '\n'.join(
            q.to_numbered_question(i) for i, q in enumerate(cases, 1)
        ) + '\n'
        expect_a = '\n'.join(
            q.to_numbered_answer(i) for i, q in enumerate(cases, 1)
        ) + '\n'
        q_path = os.path.join(DATA_DIR, "test_questions.txt")
        a_path = os.path.join(DATA_DIR, "test_answers.txt")
        with open(q_path, encoding='utf-8') as f:
            self.assertEqual(f.read(), expect_q)
        with open(a_path, encoding='utf-8') as f:
            self.assertEqual(f.read(), expect_a)


if __name__ == '__main__':
    unittest.main()
