import os

_PROGRAM_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(_PROGRAM_DIR)

QUESTION_COUNT = 50
MAX_ANSWER = 100
RESULTS_DIR = os.path.join(REPO_ROOT, "results")
QUESTIONS_FILENAME = "arithmetic_questions.txt"
ANSWERS_FILENAME = "arithmetic_answers.txt"
