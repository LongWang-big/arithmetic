from .test_arithmetic_data import generate_quiz


def run_quiz():
    """运行答题程序"""
    questions = generate_quiz()
    correct = 0

    print("=" * 50)
    print("        加减法运算练习（共100题）")
    print("=" * 50)
    print("输入答案后按回车，输入 q 退出")
    print("-" * 50)

    for i, (a, op, b, answer) in enumerate(questions, 1):
        user_input = input(f"\n第{i}题: {a} {op} {b} = ")

        if user_input.lower() == 'q':
            print("\n已退出练习")
            break

        try:
            if int(user_input) == answer:
                correct += 1
                print("✓ 正确!")
            else:
                print(f"✗ 错误! 正确答案是 {answer}")
        except ValueError:
            print("请输入有效的数字")

    print("\n" + "=" * 50)
    print(f"练习结束! 你答对了 {correct} 题")
    print("=" * 50)


if __name__ == "__main__":
    run_quiz()
