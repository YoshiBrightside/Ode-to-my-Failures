# 1200B
# Block Adventure

tests = int(raw_input())
for _ in range(tests):
    fst = list(map(int,raw_input().split()))
    heights = list(map(int,raw_input().split()))
    for i in range(len(heights)):
        if i == len(heights)-1:
            print('YES')
        else:
            if heights[i]+fst[1]+fst[2]>=heights[i+1]:
                fst[1]+=min(heights[i]+fst[2]-heights[i+1],heights[i])
                #print(fst[1])
            else:
                print('NO')
                break