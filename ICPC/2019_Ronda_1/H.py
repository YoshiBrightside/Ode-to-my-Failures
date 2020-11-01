firstLine = input().split(' ')
problems = sorted(input().split(' '))

tolerance = currentTolerance = int(firstLine[1])-1
count=0

for i in reversed(range(len(problems))):
    if (currentTolerance >= int(problems[i])):
        count+=1
        currentTolerance-=int(problems[i])
ans=str(count)

count,currentTolerance=0,tolerance
for i in range(len(problems)):
    if (currentTolerance >= int(problems[i])):
        count+=1
        currentTolerance-=int(problems[i])

# ans= ans + ' ' + str(count)
print(int(ans), int(count)) 