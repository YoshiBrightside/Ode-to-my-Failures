# 1187A
# Stickers and Toys

queries = int(input())
for x in range(queries):
    firstline = list(map(int,input().split(' ')))
    n, s, t = firstline[0], firstline[1], firstline[2]
    ans=n-s+1 if (n-s)>(n-t) else n-t+1
    print(ans)