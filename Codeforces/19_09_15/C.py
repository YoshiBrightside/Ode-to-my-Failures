#1215C
#Swap Letters

from __future__ import print_function

l = int(raw_input())
fst = raw_input()
snd = raw_input()
ans, previous, moves, doneshitb4 = 0, -1, [], False
if len(fst.split('a'))+len(snd.split('a'))%2==1 or len(fst.split('b'))+len(snd.split('b'))%2==1:
    print(-1)
    quit()
for i in range(l):
    if fst[i] != snd[i]:
        if previous != -1:
            if fst[previous]==fst[i]:
                ans+=1
                moves.append(str(previous+1)+' '+str(i+1))
            else:
                if doneshitb4:
                    aux = list(moves[-1].split())
                    moves[-2] = str(aux[0])+' '+str(i+1)
                    moves[-1] = str(aux[1])+' '+str(previous+1)
                    doneshitb4 = False
                else:
                    doneshitb4 = True
                    ans+=2
                    moves.append(str(i+1)+' '+str(i+1))
                    moves.append(str(i+1)+' '+str(previous+1))
            previous = -1
        else:
            previous = i
print(ans)
print(*moves, sep='\n')
