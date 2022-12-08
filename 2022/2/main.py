example = open("example.txt").read().strip()
input = open("input.txt").read().strip()

def part_one(file):
    scores = {"X": 1, "Y": 2, "Z": 3}
    score = 0
    for line in file.split('\n'):
        if line[0] == "A" and line[2] == "X" or \
                line[0] == "B" and line[2] == "Y" or \
                line[0] == "C" and line[2] == "Z":
            score += 3 + scores[line[2]]
        if line[0] == "A" and line[2] == "Y" or \
                line[0] == "B" and line[2] == "Z" or \
                line[0] == "C" and line[2] == "X":
            score += 6 + scores[line[2]]
        if line[0] == "A" and line[2] == "Z" or \
                line[0] == "B" and line[2] == "X" or \
                line[0] == "C" and line[2] == "Y":
            score += 0 + scores[line[2]]
    print(score)

def part_two(file):
    scores = {"A": 1, "B": 2, "C": 3}
    outcomes = {"A": ["A", "B", "C"], "B": ["B", "C", "A"], "C": ["C", "A", "B"]}
    score = 0
    for line in file.split('\n'):
        if line[2] == "X":
            score += 0 + scores[outcomes[line[0]][2]]
        if line[2] == "Y":
            score += 3 + scores[outcomes[line[0]][0]]
        if line[2] == "Z":
            score += 6 + scores[outcomes[line[0]][1]]
    print(score)

part_one(example)
part_two(example)

part_one(input)
part_two(input)
