# 2152A
# Increase or Smash

test_cases: int = int(input())
for _ in range(test_cases):
    _ = input()
    array: list = list(map(int, input().split()))
    seen: set = set()
    ans = 0
    if sum(array) == 0:
        print(0)
        break
    for _, val in enumerate(array):
        if val not in seen:
            seen.add(val)
            ans += 2
    print(ans - 1)
