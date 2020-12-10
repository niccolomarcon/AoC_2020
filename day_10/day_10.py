from collections import Counter


def one_times_three(adapters):
    adapters.sort()
    differences = [b - a for a, b in zip(adapters, adapters[1:])]
    count = Counter(differences)
    return count[1] * count[3]


if __name__ == '__main__':
    with open('input.txt') as input_file:
        adapters = list(map(int, input_file))
        adapters.append(0)  # charging outlet
        adapters.append(max(adapters) + 3)  # built-in adapter
        print(one_times_three(adapters))
