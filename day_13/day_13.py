from functools import reduce
from math import ceil, gcd, lcm


def choose_bus(time, busses):
    t_depart, bus = min((ceil(time / b) * b, b) for b in busses)
    t_wait = t_depart - time
    return t_wait * bus


def eq_class(bus):
    b, o = bus
    return (b - o, b)


def euclide(a, b):
    a, b = abs(a), abs(b)
    if a == 0:
        return (0, 1)
    else:
        x, y = euclide(b % a, a)
        return (y - (b // a) * x, x)


def solve(a, b):
    a, b = (b, a) if b[1] > a[1] else (a, b)
    rep_a, mod_a = a
    rep_b, mod_b = b
    k = (rep_a - rep_b) // gcd(mod_a, mod_b)
    x, y = euclide(mod_a, mod_b)
    solution = rep_a - k * mod_a * x
    mod_res = lcm(mod_a, mod_b)
    return (solution % mod_res, mod_res)


def contest(busses):
    rep, _ = reduce(solve, map(eq_class, busses))
    return rep


if __name__ == '__main__':
    with open('input.txt') as input_file:
        time, busses = input_file
        time = int(time)
        busses = enumerate(busses.split(','))
        busses = [(int(b), o) for o, b in busses if b != 'x']
        print(contest(busses))
