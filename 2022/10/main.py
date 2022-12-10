example = open("example.txt").read()
input = open("input.txt").read()

def part_one(file):
    registers = [1]
    lines = file.strip().split('\n')
    for line in lines:
        if line.strip() != "noop":
            registers.append(registers[-1])
            registers.append(registers[-1] + int(line.split()[1]))
        else:
            registers.append(registers[-1])
    print(sum([registers[x - 1] * x for x in range(20, 221, 40)]))

def draw(crt, registers, add):
    crt += "#" if len(crt) in range(registers[-1] - 1, registers[-1] + 2) else "."
    if len(crt) == 40:
        print(crt)
        crt = ""
    registers.append(add)
    return crt

def part_two(file):
    registers = [1]
    lines = file.strip().split('\n')
    crt = ""
    for line in lines:
        if line.strip() != "noop":
            crt = draw(crt, registers, registers[-1])
            crt = draw(crt, registers, registers[-1] + int(line.split()[1]))
        else:
            crt = draw(crt, registers, registers[-1])

part_one(example)
part_one(input)
print()
part_two(example)
part_two(input)
