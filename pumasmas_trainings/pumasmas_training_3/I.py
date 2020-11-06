countries, p, home, first = list(map(int, input().split()))
partners, num_partners, left = {}, {}, {first:1}
for _ in range(p):
    aux = list(map(int, input().split()))
    for i in range(2):
        if not partners.get(aux[i]):
            partners[aux[i]] = []
        partners[aux[i]].append(aux[1-i])
        if not num_partners.get(aux[i]):
            num_partners[aux[i]] = [0,0]
        num_partners[aux[i]][0] += 1
        num_partners[aux[i]][1] += 1
if home == first:
    print('leave')
    quit()
leaving_countries = [first]
while leaving_countries:
    leaving_country = leaving_countries.pop()
    for country in partners[leaving_country]:
        if left.get(country):
            continue
        num_partners[country][0] -= 1
        if num_partners[country][0] <= num_partners[country][1]//2:
            if country == home:
                print('leave')
                quit()
            leaving_countries.append(country)
            left[country] = 1
print('stay')