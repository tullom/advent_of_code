print("hello world")

with open("day1input.txt", 'r') as fd:
    max_calories = 0
    accum = 0
    lines = fd.readlines()
    for line in lines:
        if (line == "\n"):
            if (max_calories < accum):
                max_calories = accum
            accum = 0
            continue
        accum += int(line)

    print(max_calories)

