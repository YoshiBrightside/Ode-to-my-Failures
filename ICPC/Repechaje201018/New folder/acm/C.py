from itertools import dropwhile, takewhile

def enDias(f):
    f = [int(i) for i in f.split('/')]
    return f[0] * 1000 + (f[1] - 1) * 50 + f[2]

espec = input().split()

N = int(espec[0])
Q = int(espec[1])
inicio = espec[2]
fin = espec[3]

registros = []
busquedas = []

for i in range(N):
    registros.append((lambda r: [enDias(r[0]), int(r[1])])(input().split()[1:]))

for i in range(Q):
    b = [enDias(i) for i in input().split()[1:]]
    print(sum(
        r[1] for r in
            takewhile(lambda r: r[0] <= b[1],
                dropwhile(lambda r: r[0] < b[0], registros))
        ))