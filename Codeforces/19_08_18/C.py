# 1206C
# Almost Equal

n = int(raw_input())
if n%2==0:
    print('NO')
    quit()
ans1 = [0 for i in range(n)]
ans2 = [0 for i in range(n)]
for i in range(2*n,1,-2):
    ans1[i/2-1] = i-1 if i%4==0 else i
    ans2[i/2-1] = i-1 if i%4==2 else i
ans = ans1+ans2
print('YES')
print(str(ans).replace(',','')[1:-1])