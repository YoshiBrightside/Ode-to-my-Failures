def facMod(n):
    if n > 0:
        return (n % (10**9 + 7)) * facMod(n-1)
    elif n == 0: return 1
    else: return

espec = input().split()
N = int(espec[0])
k = int(espec[1])

print(facMod(N-1) // facMod(N-2))