"""
MST
"""
import sys
# sys.stdin = open('input.txt')

o = open('input.txt')
V,E = map(int,next(o).split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    x,y,v = map(int,next(o).split())
    graph[x].append((y, v))
    graph[y].append((x, v))
INF = int(1e9)
def prim(start):
    val = [INF]*(V+1)
    visited = [0]*(V+1)
    pair = [None]*(V+1)
    val[start] = 0
    val[0] = 0

    for i in range(1,V+1):
        minv, mindex = INF,-1
        for j in range(1,V+1):
            if not visited[j] and val[j] < minv:
                minv = val[j]
                mindex = j
        visited[mindex] = 1
        for nv,co in graph[mindex]:
            if co < val[nv] and not visited[nv]:
                val[nv] = co
                pair[nv] = mindex
    return sum(val)
print(prim(1))
