example = open("example.txt").read().split('\n\n')
input = open("input.txt").read().split('\n\n')

def part_one(elves):
    max_elf = 0

    for elf in elves:
        elf = [int(count) for count in elf.split('\n') if count != '']
        max_elf = max(max_elf, sum(elf))

    print(max_elf)

def part_two(elves):
    top_three = [0, 0, 0]

    for elf in elves:
        elf = [int(count) for count in elf.split('\n') if count != '']
        for i, cal in enumerate(top_three):
            if sum(elf) > cal:
                top_three.insert(i, sum(elf))
                top_three.pop()
                break

    print(top_three, sum(top_three))

part_one(example)
part_one(input)

part_two(example)
part_two(input)
