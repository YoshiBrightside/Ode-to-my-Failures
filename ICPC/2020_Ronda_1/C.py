import sys

def get_best_word(word, visited):
    if subs.get(word):
        return subs[word]
    ans = word
    visited[word] = 1
    for w in graph[word]:
        if visited.get(w):
            continue
        w_ans = get_best_word(w, visited)
        if len(w_ans) < len(ans):
            ans = w_ans
            continue
        if len(w_ans) == len(ans):
            ans = min(ans, w_ans)
    return ans

def fill_subs(word, sub):
    for w in graph[word]:
        if subs.get(w):
            continue
        subs[w] = sub
        fill_subs(w, sub)

graph, subs, ans = {}, {}, []
for _ in range(int(input())):
    aux = input().split()
    for i in range(2):
        if graph.get(aux[i]):
            graph[aux[i]].append(aux[1-i])
            continue
        graph[aux[i]] = [aux[1-i]]
message = input().split()
for m in message:
    if graph.get(m):
        if not subs.get(m):
            subs[m] = get_best_word(m, {})
            fill_subs(m, subs[m])
        ans.append(subs[m] + ' ')
        continue
    ans.append(m + ' ')
print(''.join(ans))

'''
print('\n FINAL')
for k, v in graph.items():
    print('graph:', k, v)
for k, v in subs.items():
    print('subs:', k, v)
    
8
sea see
see c
you u
and an
n an
are r
ok k
k z
i sea you and you are ok

4
sea see
see c
c si
si sea
'''