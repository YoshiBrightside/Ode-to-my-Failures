for case in range(int(input())):
    max_amount = list(map(int, input().split()))[1]
    queue = list(map(int, input().split()))
    for i in range(len(queue)):
        queue[i] = ((queue[i]-1)//max_amount, i+1)
    queue.sort(key= lambda x:x[1])
    queue.sort(key= lambda x:x[0])
    print('Case #', case+1, ': ', sep='', end='')
    print(*[x[1] for x in queue])
