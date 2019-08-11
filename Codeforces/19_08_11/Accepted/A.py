# 1200A
# Hotelier

_ = raw_input()
events = raw_input()
ans = [0 for i in range(10)]
for e in events:
    if e == 'L':
        for i in range(len(ans)):
            if ans[i] == 0:
                ans[i] = 1
                break
    else:
        if e == 'R':
            for i in reversed(range(len(ans))):
                if ans[i] == 0:
                    ans[i] = 1
                    break
        else:
            ans[int(e)] = 0
print(str(ans).replace(',','').replace(' ','')[1:-1])