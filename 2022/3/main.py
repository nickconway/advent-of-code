example = open("example.txt").read()
input = open("input.txt").read()

def part_one(file):
    result = 0
    for line in file.strip().split('\n'):
        half1 = set(line[:len(line) // 2])
        half2 = set(line[len(line) // 2:])
        intersection = list(half1.intersection(half2))[0]
        to_add = 0
        if intersection.islower():
            to_add = ord(intersection) - 96
        else:
            to_add = ord(intersection) - 38
        result += to_add
    print(result)
    return result

def part_two(file):
    result = 0
    group = []
    for line in file.strip().split('\n'):
        group.append(line.strip())
        if len(group) == 3:
            s1 = set(group[0])
            s2 = set(group[1])
            s3 = set(group[2])
            intersection = list(s1.intersection(s2, s3))[0]
            to_add = 0
            if intersection.islower():
                to_add = ord(intersection) - 96
            else:
                to_add = ord(intersection) - 38
            result += to_add
            group.clear()
    print(result)
    return result

part_one(example)
part_one(input)
print()
part_two(example)
part_two(input)
