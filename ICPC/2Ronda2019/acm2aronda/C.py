casesLen = int(input())
results, cases, maxnum = {}, [10]*casesLen, 1
results[maxnum] = 10
for i in range(casesLen):
    cases[i] = int(input())
orderedCases = sorted(cases)

results[orderedCases[0]] = (results[maxnum]*pow(9,orderedCases[0]-maxnum))%1000000007
results[maxnum] = results[orderedCases[0]]
maxnum = orderedCases[0]

for i in range(len(orderedCases)-1):
    if (orderedCases[i+1] not in results):
        results[orderedCases[i+1]] = (results[maxnum]*pow(9,orderedCases[i+1]-maxnum))%1000000007
        results[maxnum] = results[orderedCases[i+1]]
        maxnum = orderedCases[i+1]

print(results[cases[0]])
for i in range(len(cases)-1):
    print(results[cases[i]])