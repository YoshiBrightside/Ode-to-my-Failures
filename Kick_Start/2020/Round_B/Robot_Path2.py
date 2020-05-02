tests = int(input())
for t in range(tests):
    x_axis, y_axis, stack, multiplier = 0, 0, [], 1
    instructions = input()
    for i in range(len(instructions)):
        if instructions[i] == 'N':
            y_axis = (y_axis-multiplier)%1000000000
        elif instructions[i] == 'S':
            y_axis = (y_axis+multiplier)%1000000000
        elif instructions[i] == 'E':
            x_axis = (x_axis+multiplier)%1000000000
        elif instructions[i] == 'W':
            x_axis = (x_axis-multiplier)%1000000000
        elif instructions[i] == ')':
            multiplier /= stack.pop()
        elif instructions[i] != '(':
            multiplier *= int(instructions[i])
            stack.append(int(instructions[i]))
            i+=1
    print('Case #', t+1, ': ', int(x_axis+1), ' ', int(y_axis+1), sep='')        
