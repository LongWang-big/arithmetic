import csv
import os

from program.question import Question


class QuizFileHandler:
    """封装题目/答案的文件持久化操作。"""

    @staticmethod
    def _ensure_trailing_newline_before_append(path, block_text):
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

    def append_quiz(self, questions, question_path, answer_path):
        q_lines = [q.to_numbered_question(i) for i, q in enumerate(questions, 1)]
        a_lines = [q.to_numbered_answer(i) for i, q in enumerate(questions, 1)]
        q_block = '\n'.join(q_lines) + '\n'
        a_block = '\n'.join(a_lines) + '\n'
        q_block = self._ensure_trailing_newline_before_append(question_path, q_block)
        a_block = self._ensure_trailing_newline_before_append(answer_path, a_block)
        os.makedirs(os.path.dirname(os.path.abspath(question_path)), exist_ok=True)
        with open(question_path, 'a', encoding='utf-8') as f:
            f.write(q_block)
        with open(answer_path, 'a', encoding='utf-8') as f:
            f.write(a_block)

    @staticmethod
    def load_cases(csv_path):
        cases = []
        with open(csv_path, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cases.append(Question(
                    int(row['a']), row['op'], int(row['b']), int(row['answer']),
                ))
        return cases
