# 1197B
# Pillars

_ = int(input())
pillars = list(map(int,input().split()))
biggest = max(pillars)
bpi = pillars.index(biggest)
biggestSoFar = 0
for i in range(bpi):
    if biggestSoFar > pillars[i]:
        print('NO')
        quit()
    biggestSoFar = pillars[i]
biggestSoFar = 0
for i in reversed(range(bpi+1,len(pillars))):
    if biggestSoFar > pillars[i]:
        print('NO')
        quit()
    biggestSoFar = pillars[i]
print('YES')

