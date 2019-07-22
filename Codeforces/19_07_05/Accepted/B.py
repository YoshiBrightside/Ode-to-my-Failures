# 1189B
# Number Circle

_ = int(input())
numbers = list(reversed(sorted(list(map(int,input().split())))))
if numbers[0]>=numbers[1]+numbers[2]:
    print('NO')
else:
    print('YES') 
    last=numbers[1]
    del numbers[1]
    numbers.append(last)
    print(str(numbers)[1:-1].replace(',',''))