from itertools import combinations


def contiguous_set(ns, invalid_n):
    i, j, s = 0, 1, sum(ns[:2])
    while i < len(ns) and j < len(ns):
        if s < invalid_n:
            j += 1
            s += ns[j]
        elif s > invalid_n:
            s -= ns[i]
            i += 1
        else:
            return ns[i:j+1]
    raise Exception


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
        invalid_sum = contiguous_set(ns, invalid)
        print(min(invalid_sum) + max(invalid_sum))
