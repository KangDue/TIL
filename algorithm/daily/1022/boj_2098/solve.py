#Traveling Salesman Problem(TSP) 외판원 순회문제

o = open('input.txt')
# 비용 행렬
N = int(next(o))
W=[[*map(int,next(o).split())] for _ in range(N)]
INF=int(1e9)
#INF로 초기화하면 이미 계산을 하고 지나가도 갈수 없는 경로면 구분이 불가능함.
#계속 추가적인 계산 발생
dp = [[0]*(1<<N) for _ in range(N)]
def dfs(now,path):#now에서 시작해 now로 가는 최소비용
    if path == (1 << N) - 1: # 1111111 , bit masking으로 모든곳 방문한 경우.
        return W[now][0] or INF
    if dp[now][path]: #이미 계산한 곳이면 값 반환.
        return dp[now][path]
    limit = INF
    for i in range(1,N): #안가본 길들 하나씩 추가해보며 현재까지의 dp 최소값 갱신
        if W[now][i] and not path&(1<<i):# not (연결 x 또는 path에 이미 포함 되있다면)
            d = W[now][i] + dfs(i, path | (1 << i))
            if limit > d: limit = d
            # 현재 dp값과 , i를 출발지로 순회하는 비용 + now에서 i로 가는 비용.
    dp[now][path] = limit # 이렇게 안하고 min을 이용하면 값이 갱신 되는지 안되는지 모름.
    return limit #갱신한 dp 값 반환.
print(dfs(0,1))

# import sys
# sys.stdin = open('input.txt')
# n = int(input())
#
# INF = int(1e9)
# dp = [[0] * (1 << n) for _ in range(n)]
#
#
# def dfs(x, visited):
#     if visited == (1 << n) - 1:     # 모든 도시를 방문했다면
#         if graph[x][0]:             # 출발점으로 가는 경로가 있을 때
#             return graph[x][0]
#         else:                       # 출발점으로 가는 경로가 없을 때
#             return INF
#
#     if dp[x][visited] != INF:       # 이미 최소비용이 계산되어 있다면
#         return dp[x][visited]
#
#     limit = int(1e9)
#     for i in range(1, n):           # 모든 도시를 탐방
#         if not graph[x][i]:         # 가는 경로가 없다면 skip
#             continue
#         if visited & (1 << i):      # 이미 방문한 도시라면 skip
#             continue
#         dist = dfs(i, visited | (1 << i)) + graph[x][i]
#         if limit > dist:
#             limit = dist
#     dp[x][visited] = limit
#     return limit
#
#
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))
#
# print(dfs(0, 1))