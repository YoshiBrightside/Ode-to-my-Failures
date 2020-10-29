# NOT FINISHED. THROWS TLE

import math
import collections as c

aux = list(map(int, input().split()))
while (aux != [0, 0 , 0, 0]):
    edges, start = [[] for _ in range(aux[0])], aux[3]
    for _ in range(aux[1]):
        edge = list(map(int, input().split()))
        edges[edge[0]].append((edge[1], edge[2]))
    min_paths = [math.inf for _ in range(aux[0])]
    min_paths[start] = 0
    nodes = c.deque([start])
    visited = {}
    while nodes:
        cur_node = c.deque.popleft(nodes)
        for edge in edges[cur_node]:
            min_paths[edge[0]] = min(min_paths[edge[0]], min_paths[cur_node] + edge[1])
            if not visited.get(edge[0]):
                c.deque.append(nodes, edge[0])
    for _ in range(aux[2]):
        query = int(input())
        if min_paths[query] == math.inf:
            print('Impossible')
            continue
        print(min_paths[query])
    aux = list(map(int, input().split()))