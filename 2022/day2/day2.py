print("hello world")

# determines if won and returns a score of 6, 3, or 0
def check_if_won(opponent: str, yours: str) -> int:
    score = 0
    # opponent plays rock
    if (opponent == "A"):
        if (yours == "X"):
            score = 3
        elif (yours == "Y"):
            score = 6
        elif (yours == "Z"):
            score = 0
        else:
            #invalid input
            score = -1
    elif (opponent == "B"):
        if (yours == "X"):
            score = 0
        elif (yours == "Y"):
            score = 3
        elif (yours == "Z"):
            score = 6
        else:
            #invalid input
            score = -1
    elif (opponent == "C"):
        if (yours == "X"):
            score = 6
        elif (yours == "Y"):
            score = 0
        elif (yours == "Z"):
            score = 3
        else:
            #invalid input
            score = -1
    else:
        score = -1

    return score


with open("day2input.txt", 'r') as fd:
    total_score = 0
    lines = fd.readlines()

    for line in lines:
        if (line != "\n"):
            line = line.split(" ")
            total_score += check_if_won(line[0], line[1].strip('\n'))
            total_score += ord(line[1].strip('\n')) - 88 + 1

    print(total_score)
