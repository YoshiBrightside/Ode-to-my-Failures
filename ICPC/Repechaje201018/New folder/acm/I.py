def aBinario(oct):
    res = []
    while oct > 0:
        res.append(oct % 2)
        oct //= 2
    return list(
        reversed(
            (res + [0 for i in range(8 - len(res))])))

oct = input().split('.')

print(''.join([''.join([str(d) for d in aBinario(int(o))]) for o in oct]))