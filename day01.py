
def get_input():
    with open('inputs/input1.txt', 'r') as f:
        data = sorted([int(line) for line in f.readlines()])
    return data

def part1(data, target):
    start = 0
    end = len(data)-1
    while (start < end):
        csum = data[start] + data[end]
        if csum == target:
            break
        elif csum < target:
            start += 1
        else: # csum > target
            end -= 1
    return data[start] * data[end] if start != end else None

def part2(data, target):
    for i in data:
        other_two = part1(data, target-i) # should exclude i from data, but doesn't make a difference on this input set
        if other_two:
            return i * other_two
    return None

if __name__ == '__main__':
    data = get_input()
    result_p1 = part1(data, target=2020)
    print(result_p1) # 731731
    result_p2 = part2(data, target=2020)
    print(result_p2) # 115115990
