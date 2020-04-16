for case in range(int(input())):
    budget = int(input().split()[1])
    house_prices = sorted(map(int, input().split()))
    ans = 0
    for p in range(len(house_prices)):
        if house_prices[p] > budget:
            break
        ans += 1
        budget -= house_prices[p]
    print('Case #', case+1, ': ', ans, sep='')
    