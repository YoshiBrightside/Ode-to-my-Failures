def get_max_candy(i):
    if len(candies) <= i:
        return 0
    if max_candy[i] != 0:
        return max_candy[i]
    ans = max(candies[i] + get_max_candy(i+2), get_max_candy(i+1))
    max_candy[i] = ans
    return ans

for _ in range(int(input())):
    input()
    candies = list(map(int, input().split()))
    max_candy, ans = [0 for _ in range(len(candies))], 0
    get_max_candy(0)
    print(max(max_candy))
