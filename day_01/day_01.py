from functools import reduce
from itertools import product


def solution(expense_report, terms):
    set_er = set(expense_report)
    tuples = product(*[expense_report[:] for _ in range(terms - 1)])

    for tuple in tuples:
        friend = 2020 - sum(tuple)
        if friend in set_er:
            return reduce(lambda x, y: x * y, tuple) * friend

    raise ValueError


if __name__ == '__main__':
    with open('input.txt') as input_file:
        expense_report = [int(line) for line in input_file]

    print(solution(expense_report, 3))
