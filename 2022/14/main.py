example = open("example.txt").read()
input = open("input.txt").read()

def part_one(file):
    structures = []
    minx, maxx = 100000, -1
    miny, maxy = 100000, -1
    for i, line in enumerate(file.strip().split('\n')):
        structures.append([])
        coords = line.split(" -> ")
        for j, coord in enumerate(coords[:-1]):
            x, y = [int(c) for c in coord.split(",")]
            x2, y2 = [int(c) for c in coords[j + 1].split(",")]
            miny = min(miny, y, y2)
            maxy = max(maxy, y, y2)
            minx = min(minx, x, x2)
            maxx = max(maxx, x, x2)
            if x == x2:
                step = 1 if y < y2 else -1
                for z in range(y, y2, step):
                    structures[i].append([x, z])
            elif y == y2:
                step = 1 if x < x2 else -1
                for z in range(x, x2, step):
                    structures[i].append([z, y])
        structures[i].append([int(c) for c in coords[-1].split(",")])

    map = [["." for _ in range(minx, maxx + 1)] for _ in range(maxy + 1)]
    for structure in structures:
        for x, y in structure:
            map[y][x - minx] = "#"

    count = 0
    while True:
        try:
            sand = [0, 500 - minx]
            while True:
                newSand = sand[::]
                if map[sand[0] + 1][sand[1]] == ".":
                    newSand = [sand[0] + 1, sand[1]]
                else:
                    if map[sand[0] + 1][sand[1] - 1] == ".":
                        newSand = [sand[0] + 1, sand[1] - 1]
                    elif map[sand[0] + 1][sand[1] + 1] == ".":
                        newSand = [sand[0] + 1, sand[1] + 1]
                if newSand == sand:
                    break
                sand = newSand
            map[sand[0]][sand[1]] = "o"
            count += 1
        except:
            break
    print(count)

def part_two(file):
    structures = []
    minx, maxx = 100000, -1
    miny, maxy = 100000, -1
    for i, line in enumerate(file.strip().split('\n')):
        structures.append([])
        coords = line.split(" -> ")
        for j, coord in enumerate(coords[:-1]):
            x, y = [int(c) for c in coord.split(",")]
            x2, y2 = [int(c) for c in coords[j + 1].split(",")]
            miny = min(miny, y, y2)
            maxy = max(maxy, y, y2)
            minx = min(minx, x, x2)
            maxx = max(maxx, x, x2)
            if x == x2:
                step = 1 if y < y2 else -1
                for z in range(y, y2, step):
                    structures[i].append([x, z])
            elif y == y2:
                step = 1 if x < x2 else -1
                for z in range(x, x2, step):
                    structures[i].append([z, y])
        structures[i].append([int(c) for c in coords[-1].split(",")])

    extend = 10000
    map = [["." for _ in range(minx - extend, maxx + 1 + extend)] for _ in range(maxy + 1)]
    map.append(["." for _ in range(minx - extend, maxx + 1 + extend)])
    map.append(["#" for _ in range(minx - extend, maxx + 1 + extend)])
    for structure in structures:
        for x, y in structure:
            map[y][x - minx + extend] = "#"

    count = 0
    while True:
        sand = [0, 500 - minx + extend]
        try:
            sand = [0, 500 - minx + extend]
            while True:
                newSand = sand[::]
                if map[sand[0] + 1][sand[1]] == ".":
                    newSand = [sand[0] + 1, sand[1]]
                else:
                    if map[sand[0] + 1][sand[1] - 1] == ".":
                        newSand = [sand[0] + 1, sand[1] - 1]
                    elif map[sand[0] + 1][sand[1] + 1] == ".":
                        newSand = [sand[0] + 1, sand[1] + 1]
                if newSand == sand:
                    break
                sand = newSand
            map[sand[0]][sand[1]] = "o"
            count += 1
        except:
            break
        if sand ==[0, 500 - minx + extend]:
            break
    print(count)

part_one(example)
part_one(input)
print()
part_two(example)
part_two(input)
