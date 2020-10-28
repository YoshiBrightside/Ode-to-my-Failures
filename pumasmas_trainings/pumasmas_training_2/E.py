import collections

options, prev_animal = {}, input()
for _ in range(int(input())):
    animal = input()
    if options.get(animal[0]):
        options[animal[0]].append(animal)
    else:
        options[animal[0]] = collections.deque([animal])

if not options.get(prev_animal[-1]):
    print('?')
else:
    ans_pool = options.get(prev_animal[-1]).copy()
    while ans_pool:
        ans = ans_pool.popleft()
        if not options.get(ans[-1]) or (len(options.get(ans[-1])) == 1 and ans[0] == ans[-1]):
            print(ans+'!')
            quit()
    print(options.get(prev_animal[-1]).popleft())
