firstLine = list(map(int,raw_input().split(' ')))
testsLen, tests, results, deque = firstLine[1], [], {}, list(map(int,raw_input().split(' ')))
for i in range(testsLen):
    tests.append(int(raw_input()))

orderedTests, count = sorted(tests), 0

for i in orderedTests:
    if (i in results):
        continue
    while (count <= i):
        if (count == i):
            results[i] = str(deque[0]) + ' ' + str(deque[1])
        if (deque[0]<=deque[1]):
            deque.append(deque.pop(0))
        else:
            deque.append(deque.pop(1))
        count+=1
for i in tests:
    print (results[i])

    