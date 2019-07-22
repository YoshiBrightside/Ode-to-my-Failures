# 1197C
# Array Splitting

fst = list(map(int,input().split()))
elements = list(map(int,input().split()))
diff = [0]*(len(elements)-1)
for i in range(len(elements)-1):
    diff[i] = elements[i+1]-elements[i]
diff.sort()
print(sum(diff[:-(fst[1]-1)])) if fst[1] != 1 else print(sum(diff))