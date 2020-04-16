from __future__ import print_function

n = raw_input()
ans = list(raw_input())
count = 0
for i in range(0,len(ans)-1,2):
    if ans[i]==ans[i+1]:
        count+=1
        ans[i]='a'
        ans[i+1]='b'
print(count)
print(*ans,sep='')