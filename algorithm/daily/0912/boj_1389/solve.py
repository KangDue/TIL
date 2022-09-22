import sys
sys.stdin = open('input.txt')
"""
케빈 베이컨의 6단계 법칙
케빈 베이컨 게임은 최소 몇 단계만에 이어지는지 구하기
모든 사람과 케빈 베이컨 게임 결과의 합
플로이드 워셜 같은데 사실 이론 구현하는법은 모름 ㅋ;
유저 수 p2~100
간선 수 1~5000
"""
from collections import deque
n, m = map(int,input().split())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     x,y = map(int,input().split())
#     graph[x].append(y)
#     graph[y].append(x)
#
# def bfs(start):
#     q = deque([[start,0]])
#     visited = [0]*(n+1)
#     visited[start] = 1
#     ans = 0
#     while q:
#         v,kvn = q.popleft()
#         ans += kvn
#         for node in graph[v]:
#             if visited[node] == 0:
#                 q.append([node,kvn+1])
#                 visited[node] = 1
#     return ans
# print(min( map(lambda x:(bfs(x),x),range(1,n+1)) )[1] )

#플로이드 워셜 풀이(Floyd Warshall)
graph = [[5001]*(n+1) for _ in range(n+1)] #간선 최대 개수가 5000개이니 그거보다 크게
for _ in range(m):
    x,y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1
for k in range(1,n+1): #거쳐가는 점
    for i in range(1,n+1): #시작 점
        for j in range(1,n+1): #끝 점
            if graph[i][j] > graph[i][k] + graph[k][j]: # 경유하는 것 보다 길면
                graph[i][j] = graph[i][k] + graph[k][j]
print(min(map(lambda x:(sum(graph[x]),x),range(1,n+1)))[1] )


#    python 3 vs pypy
# fw    104ms vs 120ms
# bfs   92ms vs 144ms