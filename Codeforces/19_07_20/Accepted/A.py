# 1178A
# Prime Minister

partiesLen = int(input())
parties = list(map(int,input().split(' ')))
ans = []
total = parties[0]
ans.append(1)
for p in range(1,len(parties)):
    if parties[0] >= parties[p]*2:
        ans.append(p+1)
        total+=parties[p]
if (total > sum(parties)//2):
    print(len(ans))
    print(*ans)
else:
    print('0')