# 1186A
# Vus the Cossack and a Contest

firstline = list(map(int,input().split(' ')))
n, m, k = firstline[0], firstline[1], firstline[2]
ans = 'Yes' if (n<=m and n<=k) else 'No'
print(ans)