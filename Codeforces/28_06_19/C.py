a = str(raw_input())
b = str(raw_input())
count = 0
for x in range(len(a)-len(b)+1):
    compareA = a[x:len(b)+x]
    # diffChar = sum(int(compareA[i])^int(b[i]) for i in range(len(compareA)))
    # count+= 1 if diffChar%2==0 else 0
    # print(int(compareA))
    # print(int(b))
    # print(int(compareA,2)^int(b,2))
    count+=1 if (int(compareA,2)^int(b,2))%2==0 else 0
print(count)