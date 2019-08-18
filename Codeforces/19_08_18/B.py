# 1206B
# Make Product Equal One

_ = raw_input()
A = list(map(int,raw_input().split()))
ans = 0
negativeOnes = 0
zeroSeen = False
for a in A:
    if a > 0:
        ans += a-1
    if a < 0:
        negativeOnes += 1
        ans += -(a)-1
    if a == 0:
        ans += 1
        zeroSeen = True
if negativeOnes%2==1 and not zeroSeen:
    ans+=2
print(ans)