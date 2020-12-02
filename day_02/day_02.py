from collections import Counter


def read(line):
    policy, password = line.split(': ')
    limits, char = policy.split()
    a, b = tuple(map(int, limits.split('-')))
    return ((char, a, b), password[:-1])


def old_valid(entry):
    (char, mini, maxi), password = entry
    pass_counter = Counter(password)
    return mini <= pass_counter[char] <= maxi


def valid(entry):
    (char, i, j), password = entry
    x, y = password[i - 1], password[j - 1]
    return int(x == char) + int(y == char) == 1


if __name__ == '__main__':
    with open('input.txt') as input_file:
        policy_pass_list = [read(line) for line in input_file]
    valid_passwords = list(filter(valid, policy_pass_list))
    print(len(valid_passwords))
