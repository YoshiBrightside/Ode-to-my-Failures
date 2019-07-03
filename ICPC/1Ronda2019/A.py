frstLine = input()
scndLine = input().split(' ')

ans = 0
for i in range(len(scndLine)):
    temp, j= 0, i+1
    while(j<len(scndLine)):
        temp+= int(scndLine[j])-int(scndLine[i]) if (int(scndLine[j])-int(scndLine[i])!=-1 and int(scndLine[j])-int(scndLine[i])!=1) else 0
        j+=1
    ans += temp if (temp!=-1 and temp!=1) else 0
print(ans)
