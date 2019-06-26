# 1183D 	
# Candy Box (easy version) 

from collections import Counter

queries = int(input())
for x in range(queries):
    candiesNum = int(input())
    candies = list(map(int,input().split(' ')))
    total=Counter(candies).items()
    total.sort(key=lambda tup: tup[1])
    total.reverse()
    ans, maxCandy = 0, total[0][1]+1
    for candy in total:
        if maxCandy < 1:
            break
        if candy[1] >= maxCandy:
            maxCandy-=1
        else:
            maxCandy = candy[1]
        ans += maxCandy
    print(ans)
