example = open("example.txt").read()
input = open("input.txt").read()

def part_one(file):
    stacks = {}
    numLine = 0

    for i, line in enumerate(file.split('\n')):
        if "".join(line.split()).isdigit():
            numLine = i
            for j in range(1, int(line.strip()[-1]) + 1):
                stacks[j] = []
            break

    for line in file.split('\n')[numLine - 1::-1]:
        for key in stacks:
            index = 1 + (key - 1) * 4
            if index < len(line) and line[index] != ' ':
                stacks[key].append(line[index])

    for line in file.split('\n')[numLine + 2:-1]:
        words = line.split()
        amount = int(words[1])
        move_from = int(words[3])
        move_to = int(words[5])
        for i in range(amount):
            stacks[move_to].append(stacks[move_from].pop())

    result = ""
    for key in stacks:
        result += stacks[key][-1]

    print(result)
    return result

def part_two(file):
    stacks = {}
    numLine = 0

    lines = file.split('\n')
    for n, line in enumerate(lines):
        if "".join(line.split()).isdigit():
            numLine = n
            for i in range(int(line.strip()[-1])):
                stacks[i + 1] = [1 + 4 * i, []]
            break

    for line in lines[numLine - 1::-1]:
        for key in stacks:
            if line[stacks[key][0]] != ' ':
                stacks[key][1].append(line[stacks[key][0]])

    for line in lines[numLine + 2:-1]:
        words = line.split()
        amount = int(words[1])
        move_from = int(words[3])
        move_to = int(words[5])

        stack = []
        for i in range(amount):
            stack.append(stacks[move_from][1].pop())
        stacks[move_to][1].extend(reversed(stack))

    result = ""
    for key in stacks:
        result += stacks[key][1][-1]

    print(result)
    return result

part_one(example)
part_one(input)
print()
part_two(example)
part_two(input)
