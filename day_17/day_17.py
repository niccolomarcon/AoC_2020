from copy import deepcopy
from itertools import product, repeat
from operator import add
from sys import argv


def reach_dimensions(plane, d):
    return plane if d == 2 else {0: reach_dimensions(plane, d - 1)}


def neigh_coords(coord):
    dims = len(coord)
    zero = {tuple(repeat(0, dims))}
    deltas = set(product(*repeat([-1, 0, 1], dims))) - zero
    return [tuple(map(add, delta, coord)) for delta in deltas]


def coords(space, coord=()):
    if type(space.values().__iter__().__next__()) == dict:
        for d, plane in space.items():
            yield from coords(plane, (d, *coord))
    else:
        for d in space.keys():
            yield (d, *coord)


def getter(space, coord):
    for d in reversed(coord[1:]):
        space = space.get(d, {})
    return space.get(coord[0], '.')


def setter(space, coord, value):
    for d in reversed(coord[1:]):
        space = space.setdefault(d, {})
    space[coord[0]] = value


def cycle(hyperspace):
    new_hyperspace = deepcopy(hyperspace)
    queue, visited = set(coords(hyperspace)), set()
    while len(queue) > 0:
        coord = queue.pop()
        visited.add(coord)
        neighs = neigh_coords(coord)
        active_neighs = [getter(hyperspace, c) for c in neighs].count('#')

        if getter(hyperspace, coord) == '#':
            queue |= set(neighs) - visited

        if getter(hyperspace, coord) == '#' and active_neighs not in (2, 3):
            setter(new_hyperspace, coord, '.')
        elif getter(hyperspace, coord) == '.' and active_neighs == 3:
            setter(new_hyperspace, coord, '#')

    return new_hyperspace


def count(space):
    sample = space.values().__iter__().__next__()
    if type(sample) == dict:
        return sum(count(plane) for plane in space.values())
    else:
        return sum(1 for x in space.values() if x == '#')


def simulate(space):
    for _ in range(6):
        space = cycle(space)
    return count(space)


if __name__ == '__main__':
    with open(argv[1]) as input_file:
        lines = enumerate(input_file)
        plane = {y: {x: v for x, v in enumerate(l[:-1])} for y, l in lines}
        space = reach_dimensions(plane, 3)
        print(simulate(space))
