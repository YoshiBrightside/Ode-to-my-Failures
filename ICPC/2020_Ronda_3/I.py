books = list(map(int, input().split()))
books.sort()
i, j, cur, ans = 0, len(books)-1, 0, 0
while i-1 < j or cur >= 500:
    if cur >= 500:
        ans += cur - 100
        cur = 0
        continue
    if cur + books[j] < 500:
        cur += books[j]
        j-=1
    else:
        cur += books[i]
        i+=1
ans += cur
print(ans)