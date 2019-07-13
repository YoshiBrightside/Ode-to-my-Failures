# 1191C
# Tokitsukaze and Discard Items 

fstLine = list(map(int,input().split(' ')))
items = list(map(int,input().split(' ')))
ans, itemRange, i, counter, idk = 0, fstLine[2], 0, 0, 0
while (i<len(items)):
    if (itemRange >= items[i]):
        while (i<len(items) and itemRange >= items[i]):
            i+=1
            counter+=1
        ans+=1
        itemRange+=counter
        idk=(idk+counter)%fstLine[2]
        counter=0
    else:
        itemRange=items[i]+(fstLine[2]-(items[i]%fstLine[2]))+idk
        itemRange-=fstLine[2] if abs(items[i]-itemRange)>=fstLine[2] else 0
print(ans)
    