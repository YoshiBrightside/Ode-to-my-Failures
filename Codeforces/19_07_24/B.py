# 1196B
# Odd Sum Segments

queries = int(input())
for _ in range(queries):
    ans = []
    oddsRequired = list(map(int,input().split()))[1]
    numbers = list(map(int,input().split()))
    for i in range(len(numbers)):
        if numbers[i]%2==1:
            ans.append(i+1)
    if len(ans)<oddsRequired or (len(ans)-oddsRequired)%2==1:
        print('NO')
    else:
        print('YES')
        print(*ans[-oddsRequired:])