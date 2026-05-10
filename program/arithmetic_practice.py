"""口算练习入口：按配置生成题目，终端展示，并追加保存到 results/。"""
import os
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from program import config
from program.question_generator import QuestionGenerator
from program.storage import QuizFileHandler


class QuizApp:
    """口算练习应用，协调生成、展示与保存流程。"""

    def __init__(self):
        self.generator = QuestionGenerator(
            max_answer=config.MAX_ANSWER,
            question_count=config.QUESTION_COUNT,
        )
        self.file_handler = QuizFileHandler()
        self.question_path = os.path.join(config.RESULTS_DIR, config.QUESTIONS_FILENAME)
        self.answer_path = os.path.join(config.RESULTS_DIR, config.ANSWERS_FILENAME)

    def run(self):
        questions = self.generator.generate_quiz()
        print(f"本次练习共 {len(questions)} 道题：\n")
        for i, q in enumerate(questions, 1):
            print(f"{i}. {q.format_question()}")
        print()

        self.file_handler.append_quiz(questions, self.question_path, self.answer_path)
        print(f"题目已追加保存: {self.question_path}")
        print(f"答案已追加保存: {self.answer_path}")


if __name__ == '__main__':
    QuizApp().run()
