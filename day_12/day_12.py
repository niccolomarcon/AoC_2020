from collections import deque


move = {
    'E': lambda p, v: [p[0] + v, p[1]],
    'W': lambda p, v: [p[0] - v, p[1]],
    'N': lambda p, v: [p[0], p[1] + v],
    'S': lambda p, v: [p[0], p[1] - v],
}


def rotate(instrs):
    dir = deque('ESWN')
    for action, value in instrs:
        if action in 'EWNS':
            yield action, value
        elif action == 'F':
            yield dir[0], value
        else:
            value = 360 - value if action == 'R' else value
            dir.rotate(value // 90)


def navigate(instrs):
    pos = [0, 0]
    for action, value in rotate(instrs):
        pos = move[action](pos, value)
    return sum(map(abs, pos))


def rotate_waypoint(dir, waypoint, value):
    value = 360 - value if dir == 'R' else value
    x, y = waypoint
    rotations = deque([[x, y], [y, -x], [-x, -y], [-y, x]])
    rotations.rotate(value // 90)
    return rotations[0]


def navigate_with_waypoint(insts):
    ship = [0, 0]
    waypoint = [10, 1]
    for action, value in insts:
        if action == 'F':
            ship = [
                ship[0] + waypoint[0] * value,
                ship[1] + waypoint[1] * value
            ]
        elif action in 'EWSN':
            waypoint = move[action](waypoint, value)
        else:
            waypoint = rotate_waypoint(action, waypoint, value)
    return sum(map(abs, ship))


if __name__ == '__main__':
    with open('input.txt') as input_file:
        instrs = [(line[0], int(line[1:-1])) for line in input_file]
        print(navigate_with_waypoint(instrs))
