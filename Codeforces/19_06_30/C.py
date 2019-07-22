# 1187C
# Vasya And Array

fstline = list(map(int,input().split(' ')))
ans = [1001]*fstline[0]
for x in range(fstline[1]):
    rule = list(map(int,input().split(' ')))
    interval = range(rule[1],rule[2]) if rule[1]!=rule[2] else [rule[2]-1]
    if rule[0] == 1:
        for i in interval:
            if i>=len(ans):
                break
            if ans[i] == 1002:
                print('NO')
                quit()
            ans[i] = 1003
    else:
        for i in interval:
            if i>=len(ans):
                break
            if ans[i] == 1003:
                print('NO')
                quit()
            ans[i] = 1002
    #print(rule, ans)

ans[0]=1001
for i in range(1,len(ans)):
    if ans[i]==1003:
        ans[i]=ans[i-1]+1
    else:
        ans[i]=ans[i-1]-1
    #print(ans)

print('YES')
print(str(ans).strip('[]').replace(',',''))
