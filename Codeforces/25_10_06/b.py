'''
2145B
Deck of Cards
'''

test_cases: int = int(input())
for _ in range(test_cases):
    n, _ =  list(map(int, input().split()))
    actions =  list(input())
    result = ['+' for _ in range(n)]
    i, j = 0, len(result)-1
    seen_2s = 0
    for action in actions:
        if action == '0':
            result[i] = '-'
            i += 1
        elif action == '1':
            result[j] = '-'
            j -= 1
        else:
            seen_2s += 1

    if seen_2s > j - i:
        while i<=j:
            result[i] = '-'
            i += 1

    while seen_2s and i <= j:
        result[i] = '?'
        result[j] = '?'
        seen_2s -= 1
        i += 1
        j -= 1
    print(''.join(result))
