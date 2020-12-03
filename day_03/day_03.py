from math import prod


def count_trees(map, slope=(3, 1)):
    dx, dy = slope
    height, width = len(map), len(map[0])
    encounters = [map[y][y // dy * dx % width] for y in range(0, height, dy)]
    return sum(1 if e == '#' else 0 for e in encounters)


if __name__ == '__main__':
    with open('input.txt') as input_file:
        map = [line[:-1] for line in input_file]
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        print(prod(count_trees(map, slope) for slope in slopes))
