#1208B
#Uniqueness

_ = raw_input()
arr = list(map(int,raw_input().split()))
memo = {}
i,j = -1,-1
for n in range(len(arr)):
    if arr[n] in memo:
        if i == -1:
            i = n
        else:
            if arr[i] == arr[n]:
                j = n
            else:
                j = memo[arr[n]]
    memo[arr[n]] = n 
ans = abs(j-i)+1
memo = {}
i,j = -1,-1
for n in reversed(range(len(arr))):
    if arr[n] in memo:
        if i == -1:
            i = n
        else:
            if arr[i] == arr[n]:
                j = n
            else:
                j = memo[arr[n]]
    memo[arr[n]] = n 
if i==-1:
    print(0)
else:
    if j==-1:
        print(1)
    else:
        print(min(ans,abs(j-i)+1))