print("hello world")

stacks = [['H','B','V','W','N','M','L','P'],['M','Q','H'],['N','D','B','G','F','Q','M','L'],['Z','T','F','Q','M','W','G'],
['M','T','H','P'],['C','B','M','J','D','H','G','T'],['M','N','B','F','V','R'],['P','L','H','M','R','G','S'],['P','D','B','C','N']]
print(len(stacks))

with open("day5input.txt", 'r') as fd:
    found = 0
    lines = fd.readlines()
        

    for line in lines:
        line = line.split(' ')
        if (line == None or line[0] != "move"):
            continue
        # print(line)
        num_of_iterations = int(line[1])
        from_stack = int(line[3])-1
        to_stack = int(line[5].strip('\n'))-1
        temp_list = []
        for i in range(num_of_iterations):
            temp_list.append(stacks[from_stack].pop())
        temp_list.reverse()
        stacks[to_stack].extend(temp_list)


    for stack in stacks:
        print(stack.pop(), end="")

    print()