# 286233B
# Ehab Fails to Be Thanos

half_len = int(input())
numbers = sorted(list(map(int,input().split())))
if sum(numbers[half_len:]) != sum(numbers[:half_len]):
    print(*numbers[half_len:], *numbers[:half_len])
else:
    print(-1)