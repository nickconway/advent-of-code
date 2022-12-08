example = open("example.txt").read()
input = open("input.txt").read()

def is_visible(row, col, map):
    directions = []
    column = [row[col] for row in map]
    directions.append(map[row][col] > max(map[row][:col]))
    directions.append(map[row][col] > max(map[row][col + 1:]))
    directions.append(map[row][col] > max(column[:row]))
    directions.append(map[row][col] > max(column[row + 1:]))
    return True in directions

def get_scenic_score(row, col, map):
    column = [row[col] for row in map]
    directions = [0, 0, 0, 0]
    for tree in reversed(map[row][:col]):
        directions[0] += 1
        if tree >= map[row][col]:
            break
    for tree in map[row][col + 1:]:
        directions[1] += 1
        if tree >= map[row][col]:
            break
    for tree in reversed(column[:row]):
        directions[2] += 1
        if tree >= map[row][col]:
            break
    for tree in column[row + 1:]:
        directions[3] += 1
        if tree >= map[row][col]:
            break

    product = 1
    for dir in directions:
        product *= dir
    return product

def part_one(file):
    map = file.strip().split('\n')
    result = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if i == 0 or i == len(map) - 1 or j == 0 or j == len(map[0]) - 1:
                result += 1
            elif is_visible(i, j, map):
                result += 1
    print(result)

def part_two(file):
    map = file.strip().split('\n')
    result = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            result = max(result, get_scenic_score(i, j, map))
    print(result)

part_one(example)
part_one(input)
print()
part_two(example)
part_two(input)
