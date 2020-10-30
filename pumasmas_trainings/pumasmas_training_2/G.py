import math
import sys

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

sys.setrecursionlimit(20)
aux = list(map(int, input().split()))
while (aux != [0, 0 , 0, 0]):
    sus = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 1, 1]]#[[2,4,78],[1,0,1],[0,2,0],[3,2,59],[4,2,85],[4,1,22],[1,3,23],[0,3,43],[3,4,75],[4,0,15],[0,4,91],[3,0,16],[2,1,98],[2,3,22],[4,3,31],[0,1,0],[1,4,4],[3,1,51],[2,0,36],[1,2,59]]
    edges, start = [(0, math.inf) for _ in range(aux[0])], aux[3]
    for i in range(len(sus)):
        edge = sus[i]
        # According to Edmonds', discard edges to root
        print('trying', edge)
        if edge[1] != start and edges[edge[0]] != (edge[1], edge[2]) and edge[0] != edge[1]:
            edges[edge[1]] = min((edge[0], edge[2]), edges[edge[1]], key=lambda x: x[1])
            print(edges[edge[1]], 'defined for', edge[1])
    min_paths = [math.inf for _ in range(aux[0])]
    min_paths[start] = 0
    for _ in range(aux[2]):
        query = int(input())
        ans = get_min_path(query)
        if ans == math.inf:
            print('Impossible')
            continue
        print(ans)
    aux = list(map(int, input().split()))

'''
[[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]]
5
5
'''