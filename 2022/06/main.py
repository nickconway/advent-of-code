input = open("input.txt").read()
example = open("example.txt").read()

def part_one(input):
    seen = []
    start = 0
    i = 0
    while i < len(input):
        if input[i] not in seen:
            seen += input[i]
            i += 1
            if len(seen) == 4:
                print(i)
                return
        else:
            i = start + 1
            start = i
            while True:
                if seen.pop(0) == input[i]:
                    break

def part_two(input):
    seen = []
    start = 0
    i = 0
    while i < len(input):
        if input[i] not in seen:
            seen += input[i]
            i += 1
            if len(seen) == 14:
                print(i)
                return
        else:
            i = start + 1
            start = i
            while True:
                if seen.pop(0) == input[i]:
                    break

part_one(example)
part_one(input)
print()
part_two(example)
part_two(input)
