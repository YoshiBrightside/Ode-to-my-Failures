def getProbability(x, y):
    if x in range(l,r+1) and y in range(u,d+1):
        return 0
    if (x, y) in dp:
        return dp[x,y]
    else:
        if x == w and y == h:
            return 1
        if x == w:
            dp[x,y] = getProbability(x,y+1)
            return dp[x,y]
        if y == h:
            dp[x,y] = getProbability(x+1,y)
            return dp[x,y]
        dp[x,y] = (getProbability(x,y+1) + getProbability(x+1,y))/2
        return dp[x,y]

tests = int(input())
for t in range(tests):
    aux = list(map(int, input().split()))
    dp, w, h, l, u, r, d = {}, aux[0], aux[1], aux[2], aux[3], aux[4], aux[5]
    if (l == 1 and r == w) or (u == 1 and d == h):
        print('Case #', t+1, ': 0.0', sep='')
        continue
    ans = getProbability(1, 1)
    print('Case #', t+1, ': ', float(ans), sep='')
    