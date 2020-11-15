matrix = [[0 for _ in range(10)] for _ in range(10)]
for _ in range(int(input())):
    aux, size, x, y = list(map(int, input().split()))
    x, y = x-1, y-1
    if aux:
        for i in range(size):
            if x+i > 9 or matrix[x+i][y]:
                print('N')
                quit()
            matrix[x+i][y] = 1
    else:
        for i in range(size):
            if y+i > 9 or matrix[x][y+i]:
                print('N')
                quit()
            matrix[x][y+i] = 1
print('Y')