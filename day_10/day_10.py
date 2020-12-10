from collections import Counter


def one_times_three(adapters):
    differences = [b - a for a, b in zip(adapters, adapters[1:])]
    count = Counter(differences)
    return count[1] * count[3]


def forks(i, adapters):
    valid_next = set(adapters[i] + j for j in range(1, 4))
    for j in range(i + 1, i + 4):
        if j < len(adapters) and adapters[j] in valid_next:
            yield j


def arrangements(adapters):
    n = len(adapters) - 1
    d = {n: 1}
    for i in reversed(range(n)):
        d[i] = sum(d[v] for v in forks(i, adapters))
    return d[0]


if __name__ == '__main__':
    with open('input.txt') as input_file:
        adapters = list(map(int, input_file))
        adapters.append(0)  # charging outlet
        adapters.append(max(adapters) + 3)  # built-in adapter
        adapters.sort()
        print(arrangements(adapters))
