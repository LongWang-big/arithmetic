def format_question(a, op, b, answer=None):
    """格式化题目，带答案或不带答案"""
    if answer is not None:
        return f"{a} {op} {b} = {answer}"
    return f"{a} {op} {b} = "


def save_questions(questions, question_path, answer_path):
    """将题目和答案分别保存到文件"""
    question_lines = []
    answer_lines = []

    for i, (a, op, b, answer) in enumerate(questions, 1):
        question_lines.append(f"{i}. {format_question(a, op, b)}")
        answer_lines.append(f"{i}. {format_question(a, op, b, answer)}")

    with open(question_path, 'w') as f:
        f.write('\n'.join(question_lines))

    with open(answer_path, 'w') as f:
        f.write('\n'.join(answer_lines))
