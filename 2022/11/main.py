example = open("example.txt").read()
input = open("input.txt").read()

def part_one(file):
    monkeys = []
    for monkey in file.split('\n\n'):
        lines = monkey.split('\n')
        m = {}
        m["items"] = [int(item) for item in lines[1][18:].split(", ")]
        m["operation"] = lines[2][19:]
        m["test"] = [int(lines[3][21:]), int(lines[4][29:]), int(lines[5][30:])]
        m["inspect_count"] = 0
        monkeys.append(m)

    for i in range(1, 21):
        for j, monkey in enumerate(monkeys):
            # print(f"Monkey {j}:")
            for item in monkey["items"]:
                # print("  Monkey inspects an items with a worry level of", item)
                worry_level = eval(monkey["operation"].replace("old", str(item)))
                # print("    Worry level", worry_level)
                worry_level //= 3
                # print("    Worry level", worry_level)
                if worry_level % monkey["test"][0] == 0:
                    monkeys[monkey["test"][1]]["items"].append(worry_level)
                    # print("    Current worry level is divisible by", monkey["test"][0])
                    # print("    Item", worry_level, "thrown to monkey", monkey["test"][1])
                else:
                    monkeys[monkey["test"][2]]["items"].append(worry_level)
                    # print("    Current worry level is not divisible by", monkey["test"][0])
                    # print("    Item", worry_level, "thrown to monkey", monkey["test"][2])
                monkey["inspect_count"] += 1
            monkey["items"] = []

        # print()
        # print("After round", i)
        # for j, monkey in enumerate(monkeys):
        #     print(f"Monkey {j}:", monkey["items"])
        # print()

    max1 = 0
    max2 = 0
    for monkey in monkeys:
        if monkey["inspect_count"] > max1:
            max2 = max1
            max1 = monkey["inspect_count"]
        else:
            max2 = monkey["inspect_count"]
    print(max1 * max2)

def part_two(file):
    monkeys = []
    supermod = 1
    for monkey in file.split('\n\n'):
        lines = monkey.split('\n')
        m = {}
        m["items"] = [int(item) for item in lines[1][18:].split(", ")]
        m["operation"] = lines[2][19:]
        m["test"] = [int(lines[3][21:]), int(lines[4][29:]), int(lines[5][30:])]
        supermod *= m["test"][0]
        m["inspect_count"] = 0
        monkeys.append(m)

    for _ in range(1, 10001):
        for j, monkey in enumerate(monkeys):
            # print(f"Monkey {j}:")
            for item in monkey["items"]:
                # print("  Monkey inspects an items with a worry level of", item)
                worry_level = eval(monkey["operation"].replace("old", str(item)))
                # print("    Worry level", worry_level)
                worry_level %= supermod
                # print("    Worry level", worry_level)
                if worry_level % monkey["test"][0] == 0:
                    monkeys[monkey["test"][1]]["items"].append(worry_level)
                    # print("    Current worry level is divisible by", monkey["test"][0])
                    # print("    Item", worry_level, "thrown to monkey", monkey["test"][1])
                else:
                    monkeys[monkey["test"][2]]["items"].append(worry_level)
                    # print("    Current worry level is not divisible by", monkey["test"][0])
                    # print("    Item", worry_level, "thrown to monkey", monkey["test"][2])
                monkey["inspect_count"] += 1
            monkey["items"] = []

        # print()
        # print("After round", i)
        # for j, monkey in enumerate(monkeys):
        #     print(f"Monkey {j}:", monkey["items"])
        # print()

    max1 = 0
    max2 = 0
    for monkey in monkeys:
        if monkey["inspect_count"] > max1:
            max2 = max1
            max1 = monkey["inspect_count"]
        elif monkey["inspect_count"] > max2:
            max2 = monkey["inspect_count"]
    print(max1 * max2)

part_one(example)
part_one(input)
print()
part_two(example)
part_two(input)
