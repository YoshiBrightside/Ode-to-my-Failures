tests = int(input())
for t in range(tests):
    aux = list(map(int, input().split()))
    buses, final_day = aux[0], aux[1]
    buses_days = list(map(int, input().split()))
    ans = final_day
    for bus_day in buses_days[::-1]:
        ans -= ans%bus_day
    print('Case #', t+1, ': ', ans, sep='')        