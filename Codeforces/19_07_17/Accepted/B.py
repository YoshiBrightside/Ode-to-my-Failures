# 1195B
# Sport Mafia

fstLine = list(map(int,input().split(' ')))
turnsLeft, candies, turn = fstLine[0], 0, 1
while turnsLeft!=0 and candies-turnsLeft!=fstLine[1]:
    candies+=turn
    turn+=1
    turnsLeft-=1
print(turnsLeft)