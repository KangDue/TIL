n = 4
#음의 간선이 방향성이 없으면 무한 반복됨 = 음의 싸이클
#실제로 음의값 적절히 조절하면 싸이클도 안나타남. 정상 작동중
graph = [[],[(2,2),(4,-1),(3,1)],[(1,2),(4,1),(3,3)],\
         [(2,3),(1,3),(4,-1)],[(1,1),(2,1),(3,1)]]
# start를 정하지 않았으므로
# 무한대로 먼 임의의 정점에서 출발할때 최단거리 그래프가 됨.
dist = [1e9]*(n+1)
for i in range(n):
    for j in range(1,n+1):
        for nv,co in graph[j]:
            cost = co + dist[j]
            if dist[nv] > cost:
                dist[nv] = cost
                if i == n-1:
                    print("DETECT NEGATIVE CYCLE")
                    break
print(dist)
print(graph)
print("---------------------")
#------------------------------------------------------------------
#가정 1. 벨만 포드는 플로이드 워셔의 start 점을 고정한 간선만 살피는 개량형이다.
#검증.
INF = 1e9
graph = [[INF,INF,INF,INF,INF],
         [INF,INF,  2,  1,INF],
         [INF,  2,INF,  3,  2],
         [INF,  1,  3,INF,2],
         [INF,-2,  2,INF,INF]]
for i in range(1,n+1):
    graph[i][i] = 0
start = 1
for k in range(1,n+1):
    for j in range(1,n+1):
        cost = graph[start][k]+graph[k][j]
        if graph[start][j] > cost:
            graph[start][j] = cost
#여기서 start start 가 0보다 작으면 음의순환 발생.
print(*graph,sep='\n')


"""
결론 : 기본적으로 최단거리 탐색은 플로이드 워셜에서 출발 ( 모든 점 by 점)
-> 여기서 개량한게 벨만 포드 = 한 점 + 모든 간선(n-1 반복)
-> 다익스트라 = 음수간선 없다 가정하고 최단거리만 뽑기.
이 정도?


"""

