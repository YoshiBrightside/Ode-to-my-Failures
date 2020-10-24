import heapq

time = list(map(int, input().split()))[0]
breaks = list(map(int, input().split()))
breaks = list(zip(breaks, [i for i in range(len(breaks))]))
breaks.sort(reverse=True)
times = []
cur_time = 0
for i in range(len(breaks)):
    if len(times) >= 2:
        cur_time = heapq.heappop(times)
    heapq.heappush(times, cur_time + breaks[i][0])
    breaks[i] = (cur_time, breaks[i][1])
breaks.sort(key= lambda x: x[1])
ans = [x for x, y in breaks]
print(*ans)
