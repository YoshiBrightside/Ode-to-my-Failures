entrada = list(map(int,input().split(' ')))
daysLeft, trainsLeft, maxTolerance, trainCost, restCost, tolerance, days = entrada[0], entrada[1], entrada[2], entrada[3], entrada[4], entrada[3], 1
while(trainsLeft>0):
    if(daysLeft<trainsLeft or trainCost>maxTolerance):
        print(-1)
        exit()
    
            daysLeft-=1
            tolerance-=(days*trainCost)
            days+=1
        else: 
    else: