from functools import reduce


def calc(group):
    return len(set(group) - {'\n'})


def calc2(group):
    answers = [set(person) for person in group.strip().split('\n')]
    everyone = reduce(lambda x, y: x.intersection(y), answers)
    return len(everyone)


if __name__ == '__main__':
    with open('input.txt') as input_file:
        groups = input_file.read().split('\n\n')
        print(sum(map(calc2, groups)))
