# 1417C
# k-Amazing Numbers

for _ in range(int(input())):
    _ = int(input())
    numbers = list(map(int,input().split()))
    ans, i_due = [len(numbers)] * len(numbers), {1:ans[0]}
    ans[0] = numbers[0]
    for i in range(1, len(numbers)):
        ans = min(ans[i-1], numbers[i])
        i_due[(i+1)*2] = numbers[i]
