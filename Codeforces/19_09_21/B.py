from __future__ import print_function

_ = raw_input()
arr = list(map(int, raw_input().split()))
dic = {}
order = [0 for i in range(len(arr))]
srtarr = sorted(arr,reverse=True)
ans = 0

for i in range(len(arr)):
    if arr[i] in dic:
        dic[arr[i]].insert(0,i)
    else:
        dic[arr[i]] = [i]

for i in range(len(srtarr)):
    ans+= (i*srtarr[i])+1
    order[dic[srtarr[i]].pop()]=i+1

print(ans)
print(*order)
