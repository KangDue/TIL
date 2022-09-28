import sys
sys.stdin = open('input.txt')
"""
최소 이동 거리
0번 점에서 N번점까지 최단거리
유향그래프
"""
import heapq
to = [[1,0],[-1,0],[0,1],[0,-1]]
INF = int(1e9)
for t in range(int(input())):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        x,y,z = map(int,input().split())
        graph[x].append([y,z])
    q = [[0,0]] # dist,v
    dist = [INF]*(n+1)
    dist[0] = 1
    while q:
        d,now = heapq.heappop(q)
        if d > dist[now]:
            continue
        for nv,co in graph[now]:
                cost = d + co
                if cost < dist[nv]:
                    dist[nv] = cost
                    heapq.heappush(q,[cost,nv])
    print(f'#{t+1} {dist[n]}')