# 1196D1
# RGB Substring (easy version)


import math

for _ in range(int(input())):
    k = list(map(int,input().split()))[1]
    string = input()
    ans=math.inf
    for i in range(len(string)-k):
        sub = string[i:i+k]
        #print(sub)
        for c in range(3):
            diff = 0
            for j in range(len(sub)):
                #print('debug: '+str(j)+' '+str(c)+' '+sub[j])
                if (j+c)%3==0:
                    diff+=1 if sub[j]!='R' else 0
                if (j+c)%3==1:
                    diff+=1 if sub[j]!='G' else 0
                if (j+c)%3==2:
                    diff+=1 if sub[j]!='B' else 0
            ans = min(ans,diff)
        #print(diff)
        if ans == 0:
            break
    print(ans)