import
import collections


n, m = list(map(int, input().split()))
ans, jumps, seen = 0, {}, {}
queue = collections.deque([(0,0), (-1, -1)]) #-1, -1 is flag for other level
f_int, pl, ap = int, queue.popleft, queue.append
for i in range(n):
    aux = input()
    for j in range(len(aux)):
        jumps[(i, j)] = f_int(aux[j])
while queue:
    i, j = pl()
    if i == -1 and j == -1:
        ans += 1
        if queue:
            ap((-1, -1))
            continue
        print(-1)
        b = datetime.datetime.now() # store final time 
        print((b-a).total_seconds()) # results 
        quit()
    if i == n-1 and j == m-1:
        print(ans)
        b = datetime.datetime.now() # store final time 
        print((b-a).total_seconds()) # results 
        quit()
    seen[(i, j)] = 1
    jump = jumps[(i, j)]
    for x, y in [(i - jump, j), (i + jump, j), (i, j - jump), (i, j + jump)]:
        if 0 <= x and x < n and 0 <= y and y < m and not seen.get((x, y)):
            ap((x, y))

'''
4 3
112
212
212
210

4 5
11111
19299
19991
11110
6

5 4
1141
1999
1999
1999
1110
4

'''