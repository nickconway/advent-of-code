example = open("example.txt").read()
input = open("input.txt").read()

def part_one(file):
    max_calories = 0

    for elf in file.split('\n\n'):
        calories = sum([int(cal) for cal in elf.split('\n') if cal != ''])
        max_calories = max(max_calories, calories)

    print(max_calories)

def part_two(file):
    top_three = [0, 0, 0]

    for elf in file.split('\n\n'):
        calories = sum([int(cal) for cal in elf.split('\n') if cal != ''])
        for i, cal in enumerate(top_three):
            if calories > cal:
                top_three.insert(i, calories)
                top_three.pop()
                break

    print(sum(top_three))

part_one(example)
part_one(input)
print()
part_two(example)
part_two(input)
