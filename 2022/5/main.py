example = open("example")
input = open("input")

def run(file):
    stacks = {}

    lines = file.read().split('\n')
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
        for i in range(amount):
            stacks[move_to][1].append(stacks[move_from][1].pop())

    result = ""
    for key in stacks:
        result += stacks[key][1][-1]

    print(result)
    return result

def run2(file):
    stacks = {}

    lines = file.read().split('\n')
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

run(example)
run(input)
example.seek(0)
input.seek(0)
run2(example)
run2(input)
