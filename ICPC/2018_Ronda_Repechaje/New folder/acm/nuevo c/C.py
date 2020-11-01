def calAdder(i, ini, fin):
    if i >= len(registrosR):
        return 0
    if ini > registrosR[i]:
        return calAdder(i+1,ini,fin)
    if fin < registrosR[i]:
        return 0
    return registrosCal[i] + calAdder(i+1, ini, fin)


def enDias(f):
    f = [int(i) for i in f.split('/')]
    return f[0] * 1000 + (f[1] - 1) * 50 + f[2]


espec = input().split()

N = int(espec[0])
Q = int(espec[1])

registrosR = []
registrosCal = []
respuesta = ""

for i in range(N+Q):
    temp = input().split()
    if (temp[0]=='R') :
        registrosR.append(temp[1])
        registrosCal.append(int(temp[2]))
    else:
        b = temp[1:]
        respuesta += str(calAdder(0, b[0], b[1])) + '\n'
    

print(respuesta[:-1])
