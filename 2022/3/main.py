example = open("example.txt")
input = open("input.txt")

def run(file):
    result = 0
    for line in file:
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

run(example)
run(input)

def run2(file):
    result = 0
    group = []
    for line in file:
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

example.seek(0)
input.seek(0)
run2(example)
run2(input)
