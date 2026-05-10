"""主入口：生成题目并导出到文件"""

from .generator import generate_quiz
from .file_handler import save_questions

QUESTION_PATH = "tests/data/arithmetic_answers.txt"
ANSWER_PATH = "tests/data/arithmetic_questions.txt"


def main():
    questions = generate_quiz(50)
    save_questions(questions, QUESTION_PATH, ANSWER_PATH)
    print(f"已生成50道题，题目 -> {QUESTION_PATH}")
    print(f"答案 -> {ANSWER_PATH}")


if __name__ == "__main__":
    main()
