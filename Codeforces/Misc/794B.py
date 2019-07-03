# 764B
# Cutting Carrot

import math

fstline = list(map(float,input().split(' ')))
n, h, i, ans = fstline[0], fstline[1], 1, ''
while i < n:
    ans+=str(math.sqrt(i/n)*h)+' '
    i+=1
print(ans[:-1])
