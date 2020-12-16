from functools import partial
from heap import Heap
from itertools import chain, groupby
from math import prod
from sys import argv
import re


def extract(rule):
    regex = re.compile(r'([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)')
    match = regex.match(rule).groups()
    name, (a, b, c, d) = match[0], map(int, match[1:])
    return name, lambda x: a <= x <= b or c <= x <= d


def ticket_scanning_error_rate(rules, tickets):
    values = chain(*tickets)
    invalid = filter(lambda x: not any(r(x) for _, r in rules), values)
    return sum(invalid)


def valid(rules, ticket):
    return all(any(rule(value) for _, rule in rules) for value in ticket)


def sort_fields(indexs_per_field):
    res = [None] * len(indexs_per_field)
    heap = Heap((f, len(i)) for f, i in indexs_per_field.items())

    while not heap.empty:
        field = heap.pop()
        for other_field in heap:
            indexs_per_field[other_field] -= indexs_per_field[field]
            new_weight = len(indexs_per_field[other_field])
            heap.update(other_field, new_weight)
        index = indexs_per_field[field].pop()
        res[index] = field

    return res


def departure_multiplication(rules, ticket, nearby):
    valid_tickets = list(filter(partial(valid, rules), nearby))
    valid_tickets.append(ticket)
    columns = list(map(set, zip(*valid_tickets)))
    possible_idxs_per_field = {
        field: set(i for i, v in enumerate(columns) if all(map(rule, v)))
        for field, rule in rules
    }
    fields = sort_fields(possible_idxs_per_field)
    return prod(v for f, v in zip(fields, ticket) if f.startswith('departure'))


if __name__ == '__main__':
    with open(argv[1]) as input_file:
        groups = groupby(input_file, lambda x: x != '\n')
        rules, ticket, nearby = (list(g) for v, g in groups if v)
        rules = [extract(rule) for rule in rules]
        ticket = [int(v) for v in ticket[1].split(',')]
        nearby = [list(map(int, t.split(','))) for t in nearby[1:]]
        print(departure_multiplication(rules, ticket, nearby))
