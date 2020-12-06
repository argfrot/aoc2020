import array
from dataclasses import dataclass
import re

def get_input():
    with open('inputs/input4.txt', 'r') as f:
        data = [parse(line) for line in f.readlines()]
    return data

def test_input():
    raw = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""
    return [parse(line) for line in raw.splitlines()]

def test_all_bad():
    raw = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""
    return [parse(line) for line in raw.splitlines()]


#byr (Birth Year)
#iyr (Issue Year)
#eyr (Expiration Year)
#hgt (Height)
#hcl (Hair Color)
#ecl (Eye Color)
#pid (Passport ID)
#cid (Country ID)

@dataclass
class Passport:
    byr: int = None
    iyr: int = None
    eyr: int = None
    hgt: str = None
    hcl: str = None
    ecl: str = None
    pid: int = None
    cid: int = None

def parse(line):
    return line.strip()

def to_records(data):
    curr_record = Passport()
    for line in data:
        if not line:
            yield curr_record
            curr_record = Passport()
        else:
            for word in line.split():
                field_name, value = word.split(':')
                setattr(curr_record, field_name, value)
    if line:
        yield curr_record

def check(data, validator):
    valid = 0
    for record in to_records(data):
        if validator(record):
            valid += 1
    return valid

def validator_p1(record):
    required_attrs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all(getattr(record, attr_name) for attr_name in required_attrs)

def validator_p2(record):
    field_validators = {
        'byr': lambda x: x.isdigit() and len(x) == 4 and 1920 <= int(x) <= 2002,
        'iyr': lambda x: x.isdigit() and len(x) == 4 and 2010 <= int(x) <= 2020,
        'eyr': lambda x: x.isdigit() and len(x) == 4 and 2020 <= int(x) <= 2030,
        'hgt': lambda x: (x.endswith('cm') and x[:-2].isdigit() and 150 <= int(x[:-2]) <= 193) or (x.endswith('in') and x[:-2].isdigit() and 59 <= int(x[:-2]) <= 76),
        'hcl': lambda x: re.match('^#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$', x),
        'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda x: x.isdigit() and len(x) == 9,
    }
    required_attrs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in required_attrs:
        value = getattr(record, field)
        if value is None or not field_validators[field](value):
            return False
    return True

if __name__ == '__main__':
    data = get_input()
    result_p1 = check(data, validator=validator_p1)
    print(result_p1) # 219
    result_p2 = check(data, validator=validator_p2)
    print(result_p2) # 127
