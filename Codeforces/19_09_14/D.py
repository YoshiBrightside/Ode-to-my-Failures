#1209D
#Cow and Snacks

arr = list(map(int,raw_input().split()))
guests = [0 for i in range(arr[1])]
guestsDict = {}
snacks = [0 for i in range(arr[0])]
for i in range(arr[1]):
    guests[i] = list(map(int,raw_input().split()))
    snacks[guests[i][0]-1] += 1
    snacks[guests[i][1]-1] += 1

print(guests)
print(snacks)