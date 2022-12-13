example = open("example.txt").read()
input = open("input.txt").read()

def compare(left, right):

    for i in range(min(len(left), len(right))):
        ret = None
        if type(left[i]) == type(0) == type(right[i]):
            if left[i] == right[i]:
                continue
            return left[i] < right[i]
        elif type(left[i]) == type(0):
            ret = compare([left[i]], right[i])
        elif type(right[i]) == type(0):
            ret = compare(left[i], [right[i]])
        elif type(left[i]) == type([]) == type(right[i]):
            ret = compare(left[i], right[i])
        if ret is None:
            continue
        return ret

    if len(left) != len(right):
        return len(left) < len(right)

def part_one(file):
    in_order = []
    for i, group in enumerate(file.strip().split('\n\n')):
        left, right = group.split('\n')
        if compare(eval(left), eval(right)):
            in_order.append(i + 1)
    print(sum(in_order))


def part_two(file):
    d1 = [[2]]
    d2 = [[6]]
    n1, n2 = 1, 1
    for packet in file.replace('\n\n', '\n').strip().split('\n'):
        if compare(eval(packet), d1):
            n1 += 1
        if compare(eval(packet), d2):
            n2 += 1
    print(n1 * (n2 + 1))

part_one(example)
part_one(input)
print()
part_two(example)
part_two(input)
