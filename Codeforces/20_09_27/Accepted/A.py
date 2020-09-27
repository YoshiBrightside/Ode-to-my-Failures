# 1417A
# Copy-paste

for _ in range(int(input())):
    k = list(map(int,input().split()))[1]
    candies = list(map(int,input().split()))
    candy_to_add = min(candies)
    aux, ans = candies.index(candy_to_add), 0
    for i in range(len(candies)):
        if i == aux:
            continue
        ans += (k - candies[i]) // candy_to_add
    print(ans)