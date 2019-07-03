input()

sumaImpar = 0
sumaPar = 0
for i in range(4):
    temp = [int(i) for i in input().split()]
    if i % 2 == 0:
        sumaImpar += sum(temp[0::2])
        sumaPar += sum(temp[1::2])
    else:
        sumaImpar += sum(temp[1::2])
        sumaPar += sum(temp[0::2])

print(max([sumaImpar, sumaPar]))