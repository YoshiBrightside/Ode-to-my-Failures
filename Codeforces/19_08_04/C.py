# 1201C
# Maximum Median 

fst = list(map(int,input().split()))
extra = fst[1]
numbers = sorted(list(map(int,input().split())))
i = (len(numbers)//2)+1
possibleans = numbers[len(numbers)//2]+extra
while(i<len(numbers)):
    #print('counter: '+str(extra)+' possans: '+str(possibleans)+' '+str(numbers[i]))
    #print(possibleans<=numbers[i], possibleans<=numbers[len(numbers)//2]+fst[1])
    if possibleans<=numbers[i]: #or possibleans>numbers[len(numbers)//2]+fst[1]:
        break
    extra+=numbers[i]-numbers[len(numbers)//2]
    possibleans=numbers[len(numbers)//2]+(extra//(i+1-(len(numbers)//2)))
    i+=1
print(min(possibleans,numbers[len(numbers)//2]+fst[1]))