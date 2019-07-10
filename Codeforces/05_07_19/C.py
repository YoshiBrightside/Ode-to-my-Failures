# 1189C
# Candies!

_ = input()
numberslist = list(map(int,input().split()))
queries = int(input())
for x in range(queries):
    query = list(map(int,input().split()))
    numbers = numberslist[query[0]-1:query[1]]
    ans, i, j = 0, 0, len(numbers)
    while j>1:
        #print(*numbers)
        for i in range(j//2):
            numbers[i]=numbers[i*2]+numbers[i*2+1]
            #print(numbers[i*2], i*2, numbers[i*2+1], i*2+1)
            if numbers[i]>=10:
                numbers[i]%=10
                ans+=1
        j//=2
    #print(*numbers)
    print(ans)