from sys import argv


def play(ns, until):
    last_turn = {n: t for t, n in enumerate(ns[:-1])}
    last, start_t = ns[-1], len(ns) - 1
    for t in range(start_t, until - 1):
        next = t - last_turn.get(last, t)
        last_turn[last] = t
        last = next
    return last


if __name__ == '__main__':
    with open(argv[1]) as input_file:
        ns = list(map(int, input_file.read().split(',')))
        print(play(ns, 30000000))
