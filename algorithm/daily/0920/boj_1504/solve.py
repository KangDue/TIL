import sys
sys.stdin = open('input.txt')
"""
특정한 최단경로
무방향 그래프에서 1 -> N 정점으로 최단거리 이동
1. 임의의 두 정점 반드시 통과해야함.
2. 갔던길을 또 갈 수 있지만 반드시 최단거리 여야 한다.
#전형적인 다익스트라 ?
N = 800, E = 200000 상한선
"""
import heapq
from collections import defaultdict
o = open('input.txt')
n,e = map(int,next(o).split())
graph = [[] for i in range(n+1)]
dist = [defaultdict(int) for i in range(n+1)]
for _ in range(e):
    x,y,z = map(int,next(o).split())
    graph[x].append(y)
    graph[y].append(y)
    dist[x][y] = z
    dist[y][x] = z
v1,v2 = map(int,input().split())
q = [[2,0,1,[]]] #우선순위, 거리, 시작점,v1 이나 v2 지나면 저장
while q:
    rank,d,v,path = heapq.heappop(q)
    for nv in graph[v]:
        if dist[1][nv] > d + dist[v][nv] or dist[1][nv] == 0:
            dist[1][nv] = d + dist[v][nv]
            if nv == v1 and (v1 not in path):
                heapq.heappush(q, [rank-1,d + dist[v][nv], nv, path+[v1]])
            elif nv == v2 and (v2 not in path):
                heapq.heappush(q, [rank-1,d + dist[v][nv], nv, path+[v2]])
            else:
                heapq.heappush(q, [2-len(path),d + dist[v][nv], nv,path])
        else:
            heapq.heappush(q,[2-len(path),d+dist[v][nv], nv, path])