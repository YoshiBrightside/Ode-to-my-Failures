# 1199A
# City Day

fst = list(map(int,raw_input().split()))
days = list(map(int,raw_input().split()))
daysbefore, daysleft, ans = 0, fst[2], 1
#print(daysbefore)
for i in range(1,len(days)):
    if(daysbefore<=0 and daysleft<=0):
        print(ans)
        quit()

    if (days[i-1]>days[i]):
        if(daysleft!=fst[2]):
            daysbefore=fst[1]-1
            daysleft=fst[2]
            print('debug: going down, if, '+str(i)+': '+str(days[i])+' '+str(daysbefore)+' '+str(daysleft))
        else:
            daysbefore-=1
            ans = ans if daysbefore>0 else i+1
            print('debug: going down, else, '+str(i)+': '+str(days[i])+' '+str(daysbefore)+' '+str(daysleft))
    else:
        if(daysbefore<=0):
            if(daysleft>0):
                print('debug: going up, if, if, '+str(i)+': '+str(days[i])+' '+str(daysbefore)+' '+str(daysleft))
                daysleft-=1
            else:
                print('debug: going up, if, else, '+str(i)+': '+str(days[i])+' '+str(daysbefore)+' '+str(daysleft))
                print(ans)
                quit()
        else:
            print('debug: going up, else, '+str(i)+': '+str(days[i])+' '+str(daysbefore)+' '+str(daysleft))
            daysbefore=fst[1]-1
            daysleft=fst[2]
print(ans)