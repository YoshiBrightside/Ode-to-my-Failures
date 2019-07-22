# 1178B
# WOW Factor

strings = input().split('o')
ans, i = 0, 0
valids = []
for i in range(len(strings)):
    if len(strings[i]) > 1:
        for s in valids:
            ans+=(len(strings[s])-1)*(len(strings[i])-1)*(i-s)
            print(len(strings[s])-1, len(strings[i])-1, i-s)
        valids.append(i)
print (ans)