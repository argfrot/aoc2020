from dataclasses import dataclass
def get_input():
    with open('inputs/input2.txt', 'r') as f:
        data = [parse(line) for line in f.readlines()]
    return data

def test_input():
    raw = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""
    return [parse(line) for line in raw.splitlines()]

@dataclass
class Entry:
    range_min: int
    range_max: int
    char: str
    password: str

def parse(line):
    words = line.split()
    range = [int(x) for x in words[0].split('-')]
    char = words[1][0]
    password = words[2]
    return Entry(range[0], range[1], char, password)

def validator_p1(entry):
    n = entry.password.count(entry.char)
    return entry.range_min <= n <= entry.range_max

def validator_p2(entry):
    return (entry.password[entry.range_min-1] == entry.char) != (entry.password[entry.range_max-1] == entry.char)

def check(data, validator):
    valid = 0
    for entry in data:
        if validator(entry):
            valid += 1
    return valid

if __name__ == '__main__':
    data = get_input()
    result_p1 = check(data, validator=validator_p1)
    print(result_p1) # 586
    result_p2 = check(data, validator=validator_p2)
    print(result_p2) # 352
