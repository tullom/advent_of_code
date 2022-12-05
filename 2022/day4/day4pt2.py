print("hello world")

with open("day4input.txt", 'r') as fd:
    found = 0
    lines = fd.readlines()

    for line in lines:
        line = line.strip("\n").split(",")
        range_0_low, range_0_high = line[0].split("-")
        range_1_low, range_1_high = line[1].split("-")
        range_0_low = int(range_0_low)
        range_0_high = int(range_0_high)
        range_1_low = int(range_1_low)
        range_1_high = int(range_1_high)
        
        # check if low or high of range exists within other range
        if ((range_1_low >= range_0_low and range_1_low <= range_0_high) or (range_1_high >= range_0_low and range_1_high <= range_0_high)):
            found += 1
        elif ((range_0_low >= range_1_low and range_0_low <= range_1_high) or (range_0_high >= range_1_low and range_0_high <= range_1_high)):
            found += 1


    print(found)
