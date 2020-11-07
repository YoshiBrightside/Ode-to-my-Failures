import math

def get_min_moves(i, j, cur_moves):
    print('visiting', i, j)
    if i == n-1 and j == m-1:
        return cur_moves
    if memo.get((i, j)):
        memo[(i,j)] = min(memo[(i,j)], cur_moves)
        return memo[(i,j)]
    memo[(i, j)] = math.inf
    possibilities = [math.inf]
    if i + jumps[(i, j)] < n:
        possibilities.append(get_min_moves(i + jumps[(i, j)], j, cur_moves))
    if i - jumps[(i, j)] >= 0:
        possibilities.append(get_min_moves(i - jumps[(i, j)], j, cur_moves))
    if j + jumps[(i, j)] < m:
        possibilities.append(get_min_moves(i, j + jumps[(i, j)], cur_moves))
    if j - jumps[(i, j)] >= 0:
        possibilities.append(get_min_moves(i, j - jumps[(i, j)], cur_moves))
    memo[(i, j)] = min(possibilities)+1
    print('ans for', i, j, 'is', memo[(i, j)])
    return memo[(i,j)]


n, m = list(map(int, input().split()))
memo, jumps = {}, {}
for i in range(n):
    aux = input()
    for j in range(len(aux)):
        jumps[(i, j)] = int(aux[j])
ans = get_min_moves(0, 0, 0)
if ans == math.inf:
    ans = -1
print(ans)

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
'''