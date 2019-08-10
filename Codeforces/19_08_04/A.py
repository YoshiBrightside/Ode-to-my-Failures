# 1201A
# Important Exam

fst = list(map(int,input().split()))
answers = ['' for i in range(fst[0])]
for i in range(fst[0]):
    answers[i] = input()
value = list(map(int,input().split()))
ans = 0
for i in range(len(value)):
    counter = {}
    for j in range(len(answers)):
        if answers[j][i] in counter:
            counter[answers[j][i]]+=1
        else:
            counter[answers[j][i]]=1
    ans+=value[i]*(max(counter.values()))
print(ans)