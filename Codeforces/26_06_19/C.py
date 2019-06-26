# 1183C 	
# Computer Game 

queries = int(input())
for x in range(queries):
    line = list(map(int,input().split(' ')))
    iniCharge, turns, a, b = line[0], line[1], line[2], line[3]
    if(b*turns >= iniCharge):
        print('-1')
        continue
    turnsA = turnsB = 0
    while(turns>1):
        turnsA += turns/2+1 if turns%2==1 else turns/2
        turnsB += turns/2
        if (turnsA*a+turnsB*b >= iniCharge):
            turnsA -= turns/2+1 if turns%2==1 else turns/2
            turns -= turns/2
        else:
            turnsB -= turns/2
            turns -= turns/2+1 if turns%2==1 else turns/2
    if (turnsA*a+turnsB*b+a >= iniCharge):
        print(turnsA)
    else:
        print(turnsA+1)
