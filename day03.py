import array

def get_input():
    with open('inputs/input3.txt', 'r') as f:
        data = [parse(line) for line in f.readlines()]
    return data

def test_input():
    raw = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""
    return [parse(line) for line in raw.splitlines()]

def parse(line):
    return array.array('u', line.strip())

def check_for_trees(data, dx, dy):
    pos_x, pos_y = 0, 0
    max_y = len(data)
    max_x = len(data[0])
    hits = 0
    while (pos_y < max_y):
        hit_tree = data[pos_y][pos_x] == '#'
        if hit_tree:
            hits += 1
        #data[pos_y][pos_x] = 'X' if hit_tree else '+' # for display/debug
        pos_x = (pos_x + dx) % max_x
        pos_y += dy
    return hits

def find_best_slope(data, slopes):
    product = 0
    for slope_dx, slope_dy in slopes:
        hits = check_for_trees(data, slope_dx, slope_dy)
        product = product * hits if product else hits
    return product

if __name__ == '__main__':
    data = get_input()
    result_p1 = check_for_trees(data, dx=3, dy=1)
    print(result_p1) # 211
    result_p2 = find_best_slope(data, slopes=[(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])
    print(result_p2) # 3584591857
