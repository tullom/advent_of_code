print("hello world")

# determines if won and returns a score of 1, 2, or 3
def check_if_won(opponent: str, outcome: str) -> int:
    score = 0
    # opponent plays rock
    if (opponent == "A"):
        if (outcome == "X"):
            score = 3
        elif (outcome == "Y"):
            score = 1
        elif (outcome == "Z"):
            score = 2
        else:
            #invalid input
            score = -1
    elif (opponent == "B"):
        if (outcome == "X"):
            score = 1
        elif (outcome == "Y"):
            score = 2
        elif (outcome == "Z"):
            score = 3
        else:
            #invalid input
            score = -1
    elif (opponent == "C"):
        if (outcome == "X"):
            score = 2
        elif (outcome == "Y"):
            score = 3
        elif (outcome == "Z"):
            score = 1
        else:
            #invalid input
            score = -1
    else:
        score = -1

    score += (ord(outcome) - 88) * 3

    return score


with open("day2input.txt", 'r') as fd:
    total_score = 0
    lines = fd.readlines()

    for line in lines:
        if (line != "\n"):
            line = line.split(" ")
            total_score += check_if_won(line[0], line[1].strip('\n'))

    print(total_score)
