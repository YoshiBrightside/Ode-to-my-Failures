# 1203E
# Boxers

_ = raw_input()
boxers = list(map(int,raw_input().split()))
boxers.sort()
team = {}
team[0] = 1
for i in range(len(boxers)):
    if boxers[i]-1 not in team:
        team[boxers[i]-1] = 1
        continue
    if boxers[i] not in team:
        team[boxers[i]] = 1
        continue
    if boxers[i]+1 not in team:
        team[boxers[i]+1] = 1
        continue
print(len(team)-1)