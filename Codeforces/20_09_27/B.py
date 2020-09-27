# 1417B
# Two Arrays

for _ in range(int(input())):
    target = list(map(int,input().split()))[1]
    numbers = list(map(int,input().split()))
    n_to_target_a, n_to_target_b = {}, {}
    for n in numbers:
        if not n_to_target_a.get(n):
            n_to_target_a[target-n] = 1
            continue
        if not n_to_target_b.get(n):
            n_to_target_b[target-n] = 1
            continue
        if n_to_target_a.get(n) > n_to_target_b.get(n):
            n_to_target_b[target-n] += 1
        else:
            n_to_target_a[target-n] += 1
    ans = [0] * len(numbers)
    for i in range(len(numbers)):
        if (n_to_target_a.get(target - numbers[i]) and
            n_to_target_a[target - numbers[i]] > 0):
            ans[i] = 1
            n_to_target_a[target - numbers[i]] -= 1
    print(*ans)