from itertools import product


def apply_mask(mask, value):
    bin_v = bin(int(value))[2:].rjust(36, '0')
    masked_value = ''.join(b if m == 'X' else m for m, b in zip(mask, bin_v))
    return int(masked_value, 2)


def run(instrs):
    mask, memory = 'X' * 36, {}
    for instr, value in instrs:
        if instr == 'mask':
            mask = value
        elif instr[:3] == 'mem':
            addr = instr[4:-1]
            memory[addr] = apply_mask(mask, value)
    return memory


def apply_mask2(mask, addr, first_call=True, i=0):
    bin_a = bin(int(addr))[2:].rjust(36, '0')
    masked_a = ''.join(a if m == '0' else m for m, a in zip(mask, bin_a))
    xs = masked_a.count('X')
    for comb in product(map(str, range(2)), repeat=xs):
        res_addr = masked_a
        for c in comb:
            res_addr = res_addr.replace('X', c, 1)
        yield int(res_addr, 2)


def run2(instrs):
    mask, memory = '0' * 36, {}
    for instr, value in instrs:
        if instr == 'mask':
            mask = value
        elif instr[:3] == 'mem':
            addr = instr[4:-1]
            for addr in apply_mask2(mask, addr):
                memory[addr] = int(value)
    return memory


if __name__ == '__main__':
    with open('input.txt') as input_file:
        instrs = [line[:-1].split(' = ') for line in input_file]
        memory = run2(instrs)
        print(sum(memory[addr] for addr in memory))
