import sys
sys.stdin = open('input.txt')
"""
최소이동거리
"""
import heapq
for t in range(int(input())):
    n,e = map(int,input().split())
    graph = [[] for i in range(n+1)]
    for _ in range(e):
        x,y,z = map(int,input().split())
        graph[x].append((y,z))
    dist = [1e9]*(n+1)
    dist[0] = 0
    q = [[0,0]]
    while q:
        d,now = heapq.heappop(q)
        for nv,co in graph[now]:
            cost = d+co
            if cost < dist[nv]:
                dist[nv] = cost
                heapq.heappush(q,[cost,nv])
    print(f'#{t+1} {dist[n]}')

