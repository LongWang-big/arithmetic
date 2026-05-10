import csv
import os

from program.formatter import format_numbered_answers, format_numbered_questions


def _ensure_trailing_newline_before_append(path, block_text):
    """若文件已存在且末尾无换行，先补换行再追加块。"""
    if not block_text:
        return block_text
    if os.path.exists(path):
        with open(path, 'rb') as f:
            f.seek(0, os.SEEK_END)
            if f.tell() == 0:
                return block_text
            f.seek(-1, os.SEEK_END)
            if f.read(1) != b'\n':
                return '\n' + block_text
    return block_text


def append_quiz(questions, question_path, answer_path):
    """将一轮题目与答案以文本形式追加写入两个文件。"""
    q_lines = format_numbered_questions(questions)
    a_lines = format_numbered_answers(questions)
    q_block = '\n'.join(q_lines) + '\n'
    a_block = '\n'.join(a_lines) + '\n'
    q_block = _ensure_trailing_newline_before_append(question_path, q_block)
    a_block = _ensure_trailing_newline_before_append(answer_path, a_block)
    os.makedirs(os.path.dirname(os.path.abspath(question_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(answer_path)), exist_ok=True)
    with open(question_path, 'a', encoding='utf-8') as f:
        f.write(q_block)
    with open(answer_path, 'a', encoding='utf-8') as f:
        f.write(a_block)


def load_cases(csv_path):
    """从 CSV 加载用例，列为 a, op, b, answer。"""
    cases = []
    with open(csv_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            a = int(row['a'])
            op = row['op']
            b = int(row['b'])
            answer = int(row['answer'])
            cases.append((a, op, b, answer))
    return cases
