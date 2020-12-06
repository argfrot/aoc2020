def get_input():
    with open('inputs/input6.txt', 'r') as f:
        data = [parse(line) for line in f.readlines()]
    return data

def test_input():
    raw = """abc

a
b
c

ab
ac

a
a
a
a

b"""
    return [parse(line) for line in raw.splitlines()]

def parse(line):
    return line.strip()

def to_records(data, combine):
    curr_record = None
    for line in data:
        if not line:
            yield curr_record
            curr_record = None
        else:
            curr_record = combine(curr_record, line) if curr_record is not None else set(line)
    if line and curr_record is not None:
        yield curr_record

def check(data, combine):
    return sum(len(record) for record in to_records(data, combine))

if __name__ == '__main__':
    data = get_input()
    result_p1 = check(data, combine=lambda x,y: x.union(y))
    print(result_p1) # 7283
    result_p2 = check(data, combine=lambda x,y: x.intersection(y))
    print(result_p2) # 3520

