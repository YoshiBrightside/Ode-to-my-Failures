N, M = list(map(int, input().split()))
worker_info, subs, ans = [], {}, [0 for _ in range(N)]
for i in range(N):
    age, boss = list(map(int, input().split()))
    worker_info.append([age, boss])
    if not subs.get(boss):
        subs[boss] = []
    subs[boss].append(i+1)
for _ in range(M):
    organizer, min_age, max_age = list(map(int, input().split()))
    next_w = [organizer]
    seen = {organizer:1}
    while next_w:
        w = next_w.pop()
        ans[w-1] += 1
        w_boss = worker_info[w-1][1]
        if not seen.get(w_boss) and worker_info[w_boss-1][0] <= max_age and worker_info[w_boss-1][0] >= min_age:
            seen[w_boss] = 1
            next_w.append(w_boss)
        if subs.get(w):
            for sub in subs[w]:
                if not seen.get(sub) and worker_info[sub-1][0] <= max_age and worker_info[sub-1][0] >= min_age:
                    seen[sub] = 1
                    next_w.append(sub)
print(*ans)