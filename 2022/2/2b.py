a = open("2a.txt")
test = open("test.txt")
def run(file):
    scores = {"A": 1, "B": 2, "C": 3}
    outcomes = {"A": ["A", "B", "C"], "B": ["B", "C", "A"], "C": ["C", "A", "B"]}
    score = 0
    for line in file:
        if line[2] == "X":
            score += 0 + scores[outcomes[line[0]][2]]
        if line[2] == "Y":
            score += 3 + scores[outcomes[line[0]][0]]
        if line[2] == "Z":
            score += 6 + scores[outcomes[line[0]][1]]
    print(score)

run(test)
run(a)
