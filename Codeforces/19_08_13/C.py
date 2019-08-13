# 1203C
# Common Divisors

_ = raw_input()
numbers = list(set(list(map(int,raw_input().split()))))
smallest = min(numbers)
ans = []
for i in range(smallest,0,-1):
    if smallest%i==0:
        ans.append(i)
print(ans)