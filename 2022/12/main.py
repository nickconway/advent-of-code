example = open("example.txt").read()
input = open("input.txt").read()

def bfs(adj, start, end):
    q = [[start, 0]]
    visited = [start]
    while q:
        curr, distance = q.pop(0)
        if curr == end:
            return distance
        for node in adj[curr]:
            if node not in visited:
                q.append([node, distance + 1])
                visited.append(node)
    return float("inf")

def part_one(file):
    adj = {}
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    start, end = 0, 0

    lines = file.strip().split("\n")
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            adj[(i, j)] = set()
            height = ord(lines[i][j])
            if lines[i][j] == "S":
                start = (i, j)
                height = ord('a')
            if lines[i][j] == "E":
                end = (i, j)
                height = ord('z')

            for d in directions:
                r = i + d[0]
                c = j + d[1]
                if 0 <= r < len(lines) and 0 <= c < len(lines[0]):
                    d_height = ord('a') if lines[r][c] == "S" else ord(lines[r][c])
                    d_height = ord('z') if lines[r][c] == "E" else ord(lines[r][c])
                    if d_height < height or 0 <= d_height - height <= 1:
                        adj[(i, j)].add((r, c))

    print(bfs(adj, start, end))


def part_two(file):
    adj = {}
    starting_points = []
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    start, end = 0, 0

    lines = file.strip().split("\n")
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            adj[(i, j)] = set()
            height = ord(lines[i][j])
            if lines[i][j] == "S":
                height = ord('a')
            if lines[i][j] == "E":
                end = (i, j)
                height = ord('z')
            if lines[i][j] == "S" or lines[i][j] == "a":
                starting_points.append((i, j))

            for d in directions:
                r = i + d[0]
                c = j + d[1]
                if 0 <= r < len(lines) and 0 <= c < len(lines[0]):
                    d_height = ord('a') if lines[r][c] == "S" else ord(lines[r][c])
                    d_height = ord('z') if lines[r][c] == "E" else ord(lines[r][c])
                    if d_height < height or 0 <= d_height - height <= 1:
                        adj[(i, j)].add((r, c))

    min_steps = float('inf')
    for start in starting_points:
        steps = bfs(adj, start, end)
        if steps < min_steps:
            min_steps = steps
    print(min_steps)

part_one(example)
part_one(input)
print()
part_two(example)
part_two(input)
