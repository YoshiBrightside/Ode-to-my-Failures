#1209B
#Paint the Digits

from __future__ import print_function

for i in range(int(raw_input())):
    _ = raw_input()
    number = list(map(int,list(raw_input())))
    digitsLeft = [0 for r in range(10)]
    ans = [0 for r in range(len(number))]
    for c in range(len(number)):
        digitsLeft[number[c]] += 1
    d = 0
    while(digitsLeft[d]==0 and d<9):
        d+=1
    for c in range(len(number)):
        if (number[c]==d):
            digitsLeft[d]-=1
            ans[c] = 1
            if digitsLeft[d]<=0:
                while(digitsLeft[d]==0 and d<9):
                    d+=1
    for c in range(len(number)):
        if (number[c]==d):
            digitsLeft[d]-=1
            ans[c] = 2
            if digitsLeft[d]<=0:
                while(digitsLeft[d]==0 and d<9):
                    d+=1
    if sum(digitsLeft)>0:
        print('-')
    else:
        print(*ans, sep='')