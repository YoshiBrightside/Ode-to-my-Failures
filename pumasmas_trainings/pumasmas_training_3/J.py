import math

def get_min_moves(i, j):
    print('visiting', i, j)
    if i == n-1 and j == m-1:
        return 0
    if memo.get((i, j)):
        return memo[(i,j)]
    seen[(i, j)] = 1
    possibilities = [math.inf]
    if i + jumps[(i, j)] < n and not seen.get((i + jumps[(i, j)], j)):
        possibilities.append(get_min_moves(i + jumps[(i, j)], j))
    if i - jumps[(i, j)] >= 0 and not seen.get((i - jumps[(i, j)], j)):
        possibilities.append(get_min_moves(i - jumps[(i, j)], j))
    if j + jumps[(i, j)] < m and not seen.get((i, j + jumps[(i, j)])):
        possibilities.append(get_min_moves(i, j + jumps[(i, j)]))
    if j - jumps[(i, j)] >= 0 and not seen.get((i, j - jumps[(i, j)])):
        possibilities.append(get_min_moves(i, j - jumps[(i, j)]))
    memo[(i, j)] = min(possibilities)+1
    print('ans for', i, j, 'is', memo[(i, j)])
    return memo[(i,j)]


n, m = list(map(int, input().split()))
memo, jumps, seen = {}, {}, {}
for i in range(n):
    aux = input()
    for j in range(len(aux)):
        jumps[(i, j)] = int(aux[j])
ans = get_min_moves(0, 0)
if ans == math.inf:
    ans = -1
print(ans)

'''
4 3
112
212
212
210
'''