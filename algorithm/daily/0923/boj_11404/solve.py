import sys
# sys.stdin = open('input.txt')
"""
플로이드
주어진 버스노선 그래프에서 모든 노드간의 최단거리를 구하라
n은 정류소 수 , m은 버스 수
간선이 양방향인지 단방향인지 잘 확인!
이 문제의 경우 출발 -> 도착 으로 가는 버스 = 단방향 
그리고 갈수없는 경로는 0으로 바꿔주자
"""
o = open('input.txt')
n,m = int(next(o)),int(next(o))
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i]= 0
for _ in range(m):
    x,y,z = map(int,next(o).split())
    if graph[x][y] > z:
        graph[x][y] = z

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0

for i in range(1,n+1):
    print(*graph[i][1:])