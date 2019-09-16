#1209A
#Paint the Numbers

_ = raw_input()
arr = list(map(int,raw_input().split()))
arr.sort()
colors = {}
colors[0] = arr[0]
for i in range(len(arr)):
    c = 0
    #print('i: '+str(i)+' '+str(arr[i]))
    while c <= len(colors):
        if c != len(colors) and arr[i]%colors[c]==0:
            break
        if c == len(colors):
            colors[c] = arr[i]
            break
        #print('c: '+str(c)+' '+str(colors[c]))
        c+=1
print(len(colors))
