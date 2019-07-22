# 1195A
# Drinks Choosing

fstLine = list(map(int,input().split(' ')))
ans = 0
repetitions = [0]*(fstLine[1]+1)
setsLeft = (fstLine[0]+1)//2
for _ in range(fstLine[0]):
    repetitions[int(input())]+=1
repetitions.sort()
repetitions.reverse()
for e in repetitions:
    if e == 0:
        break
    if e > 1:
        ans+=e-(e%2)
        setsLeft-=e//2
        e%=2
if setsLeft>0:
    ans+=setsLeft
print(ans)