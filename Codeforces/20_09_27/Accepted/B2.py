# 1417B
# Two Arrays

for _ in range(int(input())):
    target = list(map(int,input().split()))[1]
    numbers = list(map(int,input().split()))
    ans, aux = [0] * len(numbers), 0
    for i in range(len(numbers)):
        if target%2 == 0 and numbers[i] == target//2:
            ans[i] = int(aux)
            aux = not aux
            continue
        if numbers[i] <= target//2:
            ans[i] = 1
    print(*ans)