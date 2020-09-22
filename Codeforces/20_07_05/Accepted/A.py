# 286233A
# 01 Game
 
for _ in range(int(input())):
    string = input()
    zeroes = len(list(string.split('0')))-1
    ones = len(string) - zeroes
    if min(zeroes, ones)%2 == 1:
        print('DA')
    else:
        print('NET')