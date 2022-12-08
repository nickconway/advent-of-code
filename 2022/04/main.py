input = open("input.txt").read()
example = open("example.txt").read()

def part_one(file):
    result = 0
    for line in file.strip().split('\n'):
        selections = line.split(",")
        for i, sel in enumerate(selections):
            selections[i] = sel.split("-")
        set1 = set([num for num in range(int(selections[0][0]), int(selections[0][1]) + 1)])
        set2 = set([num for num in range(int(selections[1][0]), int(selections[1][1]) + 1)])
        if set1.issubset(set2) or set2.issubset(set1):
            result += 1
    print(result)

def part_two(file):
    result = 0
    for line in file.strip().split('\n'):
        selections = line.split(",")
        for i, sel in enumerate(selections):
            selections[i] = sel.split("-")
        set1 = set([num for num in range(int(selections[0][0]), int(selections[0][1]) + 1)])
        set2 = set([num for num in range(int(selections[1][0]), int(selections[1][1]) + 1)])
        if set1.intersection(set2):
            result += 1
    print(result)

part_one(example)
part_one(input)
print()
part_two(example)
part_two(input)
