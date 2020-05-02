tests = int(input())
for t in range(tests):
    checkpoint_num = int(input())
    checkpoints = list(map(int, input().split()))
    ans = 0
    for i in range(1,checkpoint_num-1):
        if checkpoints[i-1] < checkpoints[i] and checkpoints[i] > checkpoints[i+1]:
            ans += 1
    print('Case #', t+1, ': ', ans, sep='')