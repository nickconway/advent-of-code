a = open("2a.txt", 'r')
test = open("test.txt", 'r')

def run(file):
    scores = {"X": 1, "Y": 2, "Z": 3}
    score = 0
    for line in file:
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

a.seek(0)
test.seek(0)
def run2(file):
    scores = {"A": 1, "B": 2, "C": 3}
    outcomes = {"A": ["A", "B", "C"], "B": ["B", "C", "A"], "C": ["C", "A", "B"]}
    score = 0
    for line in file:
        print(line)
        if line[2] == "X":
            score += 0 + scores[outcomes[line[0][2]]]
        if line[2] == "Y":
            score += 3 + scores[outcomes[line[0][0]]]
        if line[2] == "Z":
            score += 6 + scores[outcomes[line[0][1]]]
    print(score)

run(test)
run(a)
print()
run2(test)
run2(a)
