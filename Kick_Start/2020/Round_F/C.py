for case in range(int(input())):
    aux = list(map(int, input().split()))
    s, r_a, p_a, r_b, p_b, c = aux[0], aux[1], aux[2], aux[3], aux[4], aux[5]
    availability = {}
    # Check room: 1 if available, 2 if painted by alma
    # 3 if painted by bertha, else 0
    for r in range(1,s+1):
        for p in range(1,r*2):
            availability[(r, p)] = 1
    for i in range(c):
        aux = list(map(int, input().split()))
        availability[(aux[0], aux[1])] = 0
    availability[(r_a, p_a)], availability[(r_b, p_b)] = 2, 3
    if availability[(2, 2)] == 1:
        ans = 2 - c
    elif availability[(2, 2)] == 2:
        ans = min(1, 2-c)
    elif availability[(2, 2)] == 3:
        ans = -min(1, 2-c)
    else:
        ans = 0
    print('Case #', case+1, ': ', ans, sep='')