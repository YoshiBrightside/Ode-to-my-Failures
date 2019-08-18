# 1206A
# Choose Two Numbers

_ = raw_input()
A = list(map(int,raw_input().split()))
_ = raw_input()
B = list(map(int,raw_input().split()))
dic = {}
for a in A:
    dic[a] = 1
for b in B:
    dic[b] = 1

for i in range(len(A)):
    for j in range(len(B)):
        if A[i]+B[j] not in dic:
            print(str(A[i])+' '+str(B[j]))
            quit()