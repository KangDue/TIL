import sys
sys.stdin = open('input.txt')
"""
파티 N개의 숫자가 이름인 각각의 마을에 한 명의 학생이 산다.
어느날 모든 마을의 학생 N명이 마을 X 에 모여 파티를 벌이기로 했다.
마을간에는 M개의 단방향 도로 존재. 이를 지나가는데 시간 T를 소비
각 학생들 모두 최단거리로 갔다가 복귀하고 싶어하는데 이 중
가장 많은 시간을 소비하는 학생은 누구인가?
다른 도시로 가는 도로는 각 최대 1개
"""
import heapq
from collections import deque,defaultdict
n,m,x = map(int,input().split())
graph = [defaultdict() for _ in range(n+1)]
for i in range(m):
    k,y,z = map(int,input().split())
    graph[k][y]=z #단방향


dist = [0]*(n+1)
for i in range(1,n+1):
    if i != x:
        q = [[0,i]]
        visited = [0]*(n+1)
        visited[i] = 1
        while q:
            d,v = heapq.heappop(q)
            visited[v] = 1 #한 노드로 가는 경로가 여러개일 수 있다.
            if v == x:
                break
            for j in graph[v]:
                if not visited[j]:
                    heapq.heappush(q,[d+graph[v][j],j])
        dist[i] = d
dist2 = [0]*(n+1)
q = [[0, x]]
visited = [0] * (n + 1)
visited[x] = 1
while q:
    d, v = heapq.heappop(q)
    visited[v] = 1
    if dist2[v]==0: dist2[v] = d
    for j in graph[v]:
        if not visited[j]:
            heapq.heappush(q, [d + graph[v][j], j])
print(max(map(lambda x: dist[x]+dist2[x],range(1,n+1))))

#다익스트라 참조!

def dijkstra(g, start):
    d=[9876543210]*(n+1)
    d[start] = 0
    heap = [(0,start)]
    while heap:
        total, node = heappop(heap)
        if d[node]<total:continue
        for nxt, cost in g[node]:
            if d[nxt]>d[node]+cost:
                d[nxt] = d[node]+cost
                heappush(heap, (d[nxt],nxt))
    return d[1:]
