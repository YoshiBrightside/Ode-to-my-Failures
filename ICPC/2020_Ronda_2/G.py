ans, cur_ans = 100, 100
for _ in range(int(input())):
    cur_ans += int(input())
    ans = max(cur_ans, ans)
print(ans)