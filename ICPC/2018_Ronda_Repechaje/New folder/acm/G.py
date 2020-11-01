def sumN(n):
    return (n * (n+1) // 2)

def maxD(x):
    for d in range(x//2, 0, -1):
        for n in range(0, x):
            if x == d * (n+1) + sumN(n):
                return d
            elif x < d * (n+1) + sumN(n):
                break
    return -1
        

T = int(input())

distancias = []

for i in range(T):
    distancias.append(int(input()))

for i in range(T):
    print("case {0}: {1}".format(i + 1, maxD(distancias[i])))