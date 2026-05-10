"""口算练习入口：按配置生成题目，终端展示，并追加保存到 results/。"""
import os
import sys

# 支持 `python3 program/arithmetic_practice.py` 时能找到包 `program`
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from program import config
from program.formatter import format_answer, format_question
from program.question_generator import generate_quiz
from program.storage import append_quiz


def main():
    questions = generate_quiz()
    q_path = os.path.join(config.RESULTS_DIR, config.QUESTIONS_FILENAME)
    a_path = os.path.join(config.RESULTS_DIR, config.ANSWERS_FILENAME)

    print(f"本次练习共 {len(questions)} 道题：\n")
    for i, (a, op, b, _) in enumerate(questions, 1):
        print(f"{i}. {format_question(a, op, b)}")
    print()

    append_quiz(questions, q_path, a_path)
    print(f"题目已追加保存: {q_path}")
    print(f"答案已追加保存: {a_path}")


if __name__ == '__main__':
    main()
