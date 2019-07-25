# 1196B
# Robot Breakout

for _ in range(int(input())):
    robots = []
    ans = [0,0]
    for i in range(int(input())):
        line = list(map(int,input().split()))
        robots.append(line)
    robots.sort(key=lambda x: x[0])
    firstCheck, skip = True, False
    for r in robots:
        if firstCheck:
            ans[0]=r[0]
            if r[4]==1:
                continue
            else:
                firstCheck = False
        else:
            if r[2]==1 or ans[0]==r[0]:
                continue
            else:
                print(0)
                skip = True
                break
    robots.sort(key=lambda x: x[1])
    firstCheck = True
    if not skip:
        for r in robots:
            if firstCheck: 
                ans[1]=r[1]
                if r[3]==1:
                    continue
                else:  
                    firstCheck = False
            else:
                if r[5]==1 or ans[1]==r[1]:
                    continue
                else:
                    print(0)
                    break
        print('1',end=' ')
        print(*ans)