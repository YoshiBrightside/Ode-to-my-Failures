# 1197A
# DIY Wooden Ladder

queries = int(input())
for _ in range(queries):
    _ = int(input())
    planks = list(map(int,input().split()))
    planks.remove(max(planks))
    biggest = max(planks)
    planks.remove(max(planks))
    print(min(len(planks),biggest-1))