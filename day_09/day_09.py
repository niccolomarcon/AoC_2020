from itertools import combinations


def find_first_invalid(ns, preamble_length=25):
    assert len(ns) >= preamble_length
    for i, n in enumerate(ns[preamble_length:]):
        preamble = ns[i:i + preamble_length]
        sums = set(map(sum, combinations(preamble, 2)))
        if n not in sums:
            return n
    raise Exception


if __name__ == '__main__':
    with open('input.txt') as input_file:
        ns = list(map(int, input_file))
        invalid = find_first_invalid(ns)
        print(invalid)
