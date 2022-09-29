import sys
sys.stdin = open('input.txt')
"""
인수의 생일파티
인수네 마을에 N개의 집, 각 집에는 한명이 산다.
N개의 집은 각각 정점과 각 집으로의 단방향 가중치 간선
인수의 집은 X번
각 사람들은 자기 집에서 X번 집으로 왔다 갔다 한다.(최단시간)
집으로 오고가는데 가장 오래걸리는 집을 구해라.
그냥 다익스트라
"""
import heapq

INF = int(1e9)
def distance(a,b):
    q = [[0,a]]
    dist = [INF]*(n+1)
    dist[a] = 0
    while q:
        d,now = heapq.heappop(q)
        if d > dist[now]:
            continue
        if now == b:
            return d
        for nv,co in graph[now]:
            cost = d + co
            if dist[nv] > cost:
                dist[nv] = cost
                heapq.heappush(q,[cost,nv])

for t in range(int(input())):
    n,m,X = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m): #마을 사람들 관계 #전부 다른점을 주는게 아닐수도??
        x,y,z = map(int,input().split())
        graph[x].append([y,z])
    maxv = 0
    for i in range(1,n+1):
        if i == X: continue
        maxv = max(maxv,distance(i,X) + distance(X,i)) #같은 변수명을 쓰지 맙시다 ㅠㅠ
    print(f'#{t+1} {maxv}')
