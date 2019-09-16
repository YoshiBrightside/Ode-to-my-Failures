#1208A
#XORinacci

import operator

def fun(a,b,n):
    if n == 0:
        return a
    if n == 1:
        return b
    if n not in memo:
        memo[n] = operator.xor(fun(a, b, n-1), fun(a, b, n-2))
    return memo[n]

queries = int(raw_input())
global memo
memo = {}
for _ in range(queries):
    a = list(map(int,raw_input().split()))
    print(fun(a[0], a[1], a[2]))