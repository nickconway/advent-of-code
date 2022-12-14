from collections import defaultdict

example = open("example.txt").read()
input = open("input.txt").read()

def part_one(file):
    sizes = defaultdict(int)
    paths = []

    for line in file.strip().split('\n'):
        tokens = line.split()
        if tokens[0] == "$" and tokens[1] == "cd":
            if tokens[2] == "..":
                paths.pop()
            elif tokens[2] == "/":
                paths.clear()
                paths.append(tokens[2])
            elif paths[-1] == "/":
                paths.append(paths[-1] + tokens[2])
            else:
                paths.append(paths[-1] + "/" + tokens[2])
        if tokens[0].isdigit():
            for path in paths:
                sizes[path] += int(tokens[0])

    print(sum(size for size in sizes.values() if size <= 100_000))

def part_two(file):
    sizes = defaultdict(int)
    paths = []
    for line in file.strip().split('\n'):
        tokens = line.split()
        if tokens[0] == "$" and tokens[1] == "cd":
            if tokens[2] == "..":
                paths.pop()
            elif tokens[2] == "/":
                paths.clear()
                paths.append(tokens[2])
            elif paths[-1] == "/":
                paths.append(paths[-1] + tokens[2])
            else:
                paths.append(paths[-1] + "/" + tokens[2])
        if tokens[0].isdigit():
            for path in paths:
                sizes[path] += int(tokens[0])

    update_space = 30_000_000
    free = 70_000_000 - sizes["/"]
    needed = update_space - free
    print(min(size for size in sizes.values() if size > needed))

part_one(example)
part_one(input)
print()
part_two(example)
part_two(input)
