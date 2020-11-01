input()
numbers = list(map(int, input().split()))
s_numbers = sorted(numbers)
i, j, ans = 0, 0, 0
while i < len(numbers):
    if numbers[i] == s_numbers[j]:
        j += 1
        i += 1
        continue
    i += 1
    ans += 1
print(ans)
