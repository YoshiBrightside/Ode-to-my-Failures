# Unfinished :(

import math

def get_min_path(node):
    if node == start:
        return 0
    if edges[node][1] == math.inf:
        return math.inf
    if min_paths[node] != math.inf:
        return min_paths[node]
    ans = edges[node][1] + get_min_path(edges[node][0])
    min_paths[node] = ans
    return ans

aux = list(map(int, input().split()))
while (aux != [0, 0 , 0, 0]):
    edges, start, sus = [(0, math.inf) for _ in range(aux[0])], aux[3], []
    for _ in range(aux[1]):
        sus.append(list(map(int, input().split())))
    sus.sort(key=lambda x: x[2], reverse=True)
    while sus:
        edge = sus.pop()
        # According to Edmonds', discard edges to root
        if edge[1] != start and (edges[edge[0]][1] == math.inf or edges[edge[0]][1] == math.inf):
            edges[edge[1]] = min((edge[0], edge[2]), edges[edge[1]], key=lambda x: x[1])
    min_paths = [math.inf for _ in range(aux[0])]
    min_paths[start] = 0
    for e in edges:
        print(e)
    for _ in range(aux[2]):
        visited = {}
        query = int(input())
        ans = get_min_path(query)
        if ans == math.inf:
            print('Impossible')
            continue
        print(ans)
    aux = list(map(int, input().split()))