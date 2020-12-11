from collections import Counter
from itertools import chain, product


EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'


def step(grid, r, c, rs, cs):
    neigh_is = set(product(range(r-1, r+2), range(c-1, c+2))) - {(r, c)}
    valid_is = filter(lambda p: 0 <= p[0] < rs and 0 <= p[1] < cs, neigh_is)
    neigh_count = Counter(grid[r][c] for r, c in valid_is)

    if grid[r][c] == EMPTY and neigh_count[OCCUPIED] == 0:
        return OCCUPIED
    elif grid[r][c] == OCCUPIED and neigh_count[OCCUPIED] >= 4:
        return EMPTY
    else:
        return grid[r][c]


def gol(grid, rows, cols):
    rs, cs = range(rows), range(cols)
    next_grid = [[step(grid, r, c, rows, cols) for c in cs] for r in rs]
    return grid if grid == next_grid else gol(next_grid, rows, cols)


def count_occupied_after_settling(ferry):
    rows, cols = len(ferry), len(ferry[0])
    settled_ferry = gol(ferry, rows, cols)
    counter = Counter(chain(*settled_ferry))
    return counter[OCCUPIED]


if __name__ == '__main__':
    with open('input.txt') as input_file:
        ferry = [list(line[:-1]) for line in input_file]
        print(count_occupied_after_settling(ferry))
