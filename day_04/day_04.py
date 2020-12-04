import re


def valid_hgt(x):
    n, m = x[:-2], x[-2:]
    v = n.isdigit()
    if m == 'cm':
        return v and 150 <= int(n) <= 193
    elif m == 'in':
        return v and 59 <= int(n) <= 76
    else:
        return False


NINE_DIGITS_RE = re.compile(r'^\d{9}$')
RGB_RE = re.compile(r'^#[0-9a-f]{6}$')
FIELDS = {
    'byr': lambda x: x.isdigit() and 1920 <= int(x) <= 2002,
    'iyr': lambda x: x.isdigit() and 2010 <= int(x) <= 2020,
    'eyr': lambda x: x.isdigit() and 2020 <= int(x) <= 2030,
    'hgt': valid_hgt,
    'hcl': lambda x: RGB_RE.match(x),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: NINE_DIGITS_RE.match(x)
}


def valid(passport):
    try:
        for field, validator in FIELDS.items():
            if not validator(passport[field]):
                return False
        return True
    except Exception:
        return False


if __name__ == '__main__':
    passports = []
    with open('input.txt') as input_file:
        current_passport = {}
        for line in input_file:
            if line == '\n':
                passports.append(current_passport)
                current_passport = {}
            else:
                for key_val_pair in line[:-1].split():
                    key, value = key_val_pair.split(':')
                    current_passport[key] = value
        passports.append(current_passport)

    print(len(list(filter(valid, passports))))
