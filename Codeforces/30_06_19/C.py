# 1187C
# Vasya And Array

fstline = list(map(int,input().split(' ')))
ans = [1]*fstline[0]
for x in range(fstline[1]):
    rule = list(map(int,input().split(' ')))
    interval = range(rule[1],rule[2]-1) if rule[1]!=rule[2]-1 else [rule[2]-1]
    if rule[0] == 1:
        for i in interval:
            # print(i)
            if ans[i] == 2:
                print('NO')
                quit()
            ans[i] = 3
    else:
        for i in interval:
            if ans[i] == 3:
                print('NO')
                quit()
            ans[i] = 2
    # print(rule, ans)

ans[0]=1
for i in range(1,len(ans)):
    if ans[i]==3:
        ans[i]=ans[i-1]+1
    else:
        ans[i]=ans[i-1]

print('YES')
print(str(ans).strip('[]').strip(','))
