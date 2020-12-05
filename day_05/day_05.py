from functools import reduce


def next_range(r, x):
    start, end = r
    middle = start + (end - start) // 2
    return (start, middle) if x in ('F', 'L') else (middle + 1, end)


def row(s):
    return reduce(next_range, s[:7], (0, 127))[0]


def column(s):
    return reduce(next_range, s[7:], (0, 7))[0]


def id(s):
    return row(s) * 8 + column(s)


if __name__ == '__main__':
    with open('input.txt') as input_file:
        seats = input_file.read().splitlines()
        ids = sorted(map(id, seats))
        for id_i, id_j in zip(ids, ids[1:]):
            if (my_id := id_i + 1) != id_j:
                print(my_id)
