# 1203B
# Equal Rectangles

queries = int(raw_input())
for _ in range(queries):
    squares = int(raw_input())
    sticks = list(map(int,raw_input().split()))
    sticks.sort()
    squareArea = sticks[0]*sticks[len(sticks)-1]
    failed=False
    for i in range(0,len(sticks)/2,2):
        if sticks[i]!=sticks[i+1] or sticks[len(sticks)-i-1]!=sticks[len(sticks)-i-2] or sticks[i]*sticks[len(sticks)-i-1]!=squareArea:
            failed=True
            break
    print('YES') if not failed else 'NO'

    