def get_input():
    with open('inputs/input5.txt', 'r') as f:
        data = [parse(line) for line in f.readlines()]
    return data

def test_input():
    raw = """"""
    return [parse(line) for line in raw.splitlines()]

def parse(line):
    return line.strip()

def seat_number(raw: str):
    val, column_val = 0, 1
    for digit in reversed(raw):
        if digit in 'RB':
            val += column_val
        column_val *= 2
    return val

def find_highest_seat(data):
    return max(seat_number(raw) for raw in data)

def find_missing_seat(data):
    prev = None
    for seat in sorted(seat_number(raw) for raw in data):
        if prev and seat != prev+1:
            return prev+1
        prev = seat
    return None

if __name__ == '__main__':
    data = get_input()
    result_p1 = find_highest_seat(data)
    print(result_p1) # 965
    result_p2 = find_missing_seat(data)
    print(result_p2) # 524
    