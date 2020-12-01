from itertools import product


def solution(expense_report):
    set_er = set(expense_report)
    partial_sums = list(product(expense_report, expense_report))

    assert len(set_er) == len(expense_report)  # -> all the numbers are unique

    for a, b in partial_sums:
        friend = 2020 - a - b
        if friend in set_er:
            return a * b * friend

    raise ValueError


if __name__ == '__main__':
    with open('input.txt') as input_file:
        expense_report = [int(line) for line in input_file]

    print(solution(expense_report))
