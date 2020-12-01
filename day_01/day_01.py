def solution(expense_report):
    set_er = set(expense_report)
    assert len(set_er) == len(expense_report)  # -> all the numbers are unique

    for number in expense_report:
        friend = 2020 - number
        if friend in set_er:
            return friend * number

    raise ValueError


if __name__ == '__main__':
    with open('input.txt') as input_file:
        expense_report = [int(line) for line in input_file]

    print(solution(expense_report))
