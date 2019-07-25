# 1196A
# Three Piles of Candies

queries = int(input())
for _ in range(queries):
    line = list(map(int,input().split()))
    print(sum(line)//2)