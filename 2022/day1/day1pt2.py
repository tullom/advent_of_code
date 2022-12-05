print("hello world")

with open("day1input.txt", 'r') as fd:
    total_calories_list = []    # total calories carried by each elf
    max_calories = 0
    accum = 0
    lines = fd.readlines()
    for line in lines:
        if (line == "\n"):
            total_calories_list.append(accum)
            accum = 0
        else:
            accum += int(line)

    accum = 0
    for i in range(3):
        accum += total_calories_list.pop(total_calories_list.index(max(total_calories_list)))
    
    print(accum)
        