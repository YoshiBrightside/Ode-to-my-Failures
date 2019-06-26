# 1183B
# Equalize Prices 

queries = int(input())
for x in range(queries):
    maxDiff = list(map(int,input().split(' ')))[1]
    prices = list(map(int,input().split(' ')))
    minPrice = min(prices)
    maxPrice = max(prices)
    if (minPrice+maxDiff < maxPrice-maxDiff):
        print('-1')
        continue
    print(minPrice+maxDiff)
