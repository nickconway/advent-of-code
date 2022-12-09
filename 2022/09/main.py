example = open("example.txt").read()
input = open("input.txt").read()

def part_one(file):
    directions = {"L": [-1, 0], "R": [1, 0], "U": [0, 1], "D": [0, -1]}
    head = [0, 0]
    tail = [0, 0]
    tail_path = set()
    tail_path.add(tuple(tail))
    for line in file.strip().split('\n'):
        for _ in range(int(line.split()[1])):
            head_prev = [head[0], head[1]]
            head[0] += directions[line[0]][0]
            head[1] += directions[line[0]][1]
            if abs(tail[0] - head[0]) > 1 or abs(tail[1] - head[1]) > 1:
                tail = head_prev
            tail_path.add(tuple(tail))
    print(len(tail_path))

def part_two(file):
    directions = {"L": [-1, 0], "R": [1, 0], "U": [0, 1], "D": [0, -1]}
    knots = [[0, 0] for _ in range(10)]
    tail_path = set()
    tail_path.add((0, 0))
    for line in file.strip().split('\n'):
        for _ in range(int(line.split()[1])):
            knots[0][0] += directions[line[0]][0]
            knots[0][1] += directions[line[0]][1]
            for i in range(1, 10):
                dx = knots[i - 1][0] - knots[i][0]
                dy = knots[i - 1][1] - knots[i][1]
                if abs(dx) > 1 or abs(dy) > 1:
                    knots[i][0] += (1 if dx > 0 else 0 if dx == 0 else - 1)
                    knots[i][1] += (1 if dy > 0 else 0 if dy == 0 else - 1)
            tail_path.add(tuple(knots[-1]))
    print(len(tail_path))

part_one(example)
part_one(input)
print()
part_two(example)
part_two(input)
