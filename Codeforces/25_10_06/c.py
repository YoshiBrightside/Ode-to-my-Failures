'''
2145C
Monocarp's String
'''

test_cases: int = int(input())
for _ in range(test_cases):
    _ = input()
    s = input()
    seen, max_cons, cur_cons, last_seen = {'a': 0, 'b': 0}, {'a': 0, 'b': 0}, 0, ''
    for c in s:
        seen[c] += 1
        if last_seen == c:
            cur_cons += 1
            max_cons[c] = max(cur_cons, max_cons[c])
        else:
            last_seen = c
            cur_cons = 1
            max_cons[c] = max(cur_cons, max_cons[c])
    
    if seen['a'] == 0 or seen['b'] == 0:
        print(-1)
    elif seen['a'] == seen['b']:
        print(0)
    else:
        if seen['a'] > seen['b']:
            if max_cons['a'] >= seen['a'] - seen['b']:
                print(seen['a']-seen['b'])
            else:
                print(-1)
        if seen['b'] > seen['a']:
            if max_cons['b'] >= seen['b'] - seen['a']:
                print(seen['b']-seen['a'])
            else:
                print(-1)
            
