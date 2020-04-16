from __future__ import print_function
from fractions import gcd
from functools import reduce


ans = []
size = int(raw_input())
matrix = [[] for x in range(size)]
for i in range(size):
    matrix[i] = list(map(int,raw_input().split()))
for i in range(size):
    matrix[i][i] = reduce(gcd,matrix[i][i+1:]+list(matrix[j][i] for j in range(i)))
    ans.append(matrix[i][i])
print(*matrix)
print(*ans)