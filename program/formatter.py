def format_question(a, op, b):
    return f"{a} {op} {b} = "


def format_answer(a, op, b, answer):
    return f"{a} {op} {b} = {answer}"


def format_numbered_questions(questions):
    """questions: list of (a, op, b, answer)"""
    return [
        f"{i}. {format_question(a, op, b)}"
        for i, (a, op, b, _) in enumerate(questions, 1)
    ]


def format_numbered_answers(questions):
    return [
        f"{i}. {format_answer(a, op, b, ans)}"
        for i, (a, op, b, ans) in enumerate(questions, 1)
    ]
