queries = int(input())
numbers = [0]*queries
for x in range(queries):
    numbers[x]= float(input())
ordNum = sorted(numbers)
i, j, difference = 0, len(numbers), 0
print(ordNum)
while(i!=j):
    if(abs(total+ordNum[i])>abs(total+ordNum[j])):
        ordNum[i],ordNum[j]=int(ordNum[i]),int(ordNum[j])+1
    elif()
