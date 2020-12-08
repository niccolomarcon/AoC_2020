def do(action, value, acc, i):
    if action == 'acc':
        acc += value
    elif action == 'jmp':
        i += value - 1
    elif action == 'nop':
        pass
    return acc, i


def run(instrs):
    visited, acc, i = set(), 0, 0
    while i < len(instrs):
        if i in visited:
            break
        else:
            visited.add(i)
            action, value = instrs[i]
            acc, i = do(action, int(value), acc, i)
            i += 1
    else:
        return acc, True
    return acc, False


if __name__ == '__main__':
    with open('input.txt') as input_file:
        instructions = [tuple(line.split()) for line in input_file]
        changeble = [i for i, (action, _) in enumerate(instructions) if action in ('nop', 'jmp')]
        for i in changeble:
            old_action, value = instructions[i]
            new_action = 'jmp' if old_action == 'nop' else 'nop'
            instructions[i] = new_action, value
            res, terminated = run(instructions)
            if terminated:
                print(res)
                break
            else:
                instructions[i] = old_action, value
