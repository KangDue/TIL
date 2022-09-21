import sys
# sys.stdin = open('input.txt')
"""
방향 그래프에서 시작점부터 다른 모든 정점으로 최단경로 구하기
전형적인 다익스트라.
"""
import heapq
o = open('input.txt')
v,e = map(int,next(o).split())
start =int( next(o) )
graph=[[] for i in range(v+1)]
dist = ['INF']*(v+1)
for _ in range(e):
    x,y,z = map(int,next(o).split())
    graph[x].append((y,z)) # 방향성 그래프
q = [[0,start]]
dist[start] = 0
while q:
    d,now = heapq.heappop(q)
    for nv,co in graph[now]:
        cost = d+co
        if dist[nv] == 'INF' or dist[nv] > cost:
            dist[nv] = cost
            heapq.heappush(q,[cost,nv])
print(*dist[1:],sep='\n')
# print(*map(lambda x:'INF' if x==1e+10 else x,dist[1:]),sep='\n') #for if보다 연산이 늘어서 조금 더 오래걸림
# 처음부터 큰값을 INF로 놓으면 빠르지 않을까? ㄱㄱ
