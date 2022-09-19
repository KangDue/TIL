import sys
# sys.stdin = open('input.txt')
"""
트리의 지름, 트리에서 임의의 두 점 중 거리가 가장 먼 점
일단 플로이드 워셜로 도전
입력이 10만개 까지도 주어져서 open 활용
하려했지만 플로이드 워셜 갈기면 10만 세제곱 수준이라 그건좀 ... 그래도 시도 -> 바로 메모리초과 
"""

#플로이드 워셜 버전- 메모리 초과
# o = open('input.txt')
# n = int(next(o))
# grid = [[10001*n*n]*(n+1) for i in range(n+1)]
# s = 1
# for i in o:
#     info = [*map(int,i.split())]
#     for i in range(1,len(info)-1,2):
#         s+=info[i+1]
#         grid[info[0]][info[i]] = info[i+1]
#         grid[info[i]][info[0]] = info[i+1]
# # print(*grid,sep='\n')
# mv = 0
# for k in range(1,n+1):
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if i != j:
#                 if grid[i][j] > grid[i][k]+grid[k][j]:
#                     grid[i][j] = grid[i][k]+grid[k][j]
#                 if grid[i][j] < s:mv=max(mv,grid[i][j])
# # print(*grid,sep='\n')
# print(mv)

#-------------------------------------------------
#우연히 어떤 랭커분의 글을 봐버렸다 ....
#한 점 기준으로 제일 먼 곳 찾고, 그 점 기준으로 제일 먼 곳 찾고 더하기
# from collections import defaultdict as dd
# import heapq #최소힙이라 마지막에 남은게 최대거리라 편하긴 한데 , 속도가 느림. #그냥 deque쓰는게 더빠르다
#어차피 전부다 탐색은 하니까
# o = open('input.txt')
# n = int(next(o))
# linked = [dd(int) for i in range(n+1)]
# for i in o:
#     info = [*map(int,i.split())]
#     for i in range(1,len(info)-1,2):
#         linked[info[0]][info[i]] = info[i+1]
#         linked[info[i]][info[0]] = info[i+1]
# for i in range(1,n+1):
#     if linked[i]:
#         q = [[0,i]]
#         visited = [0] * (n + 1)
#         visited[i] = 1
#         while q:
#             d,v = heapq.heappop(q)
#             for node in linked[v]:
#                 if not visited[node]:
#                     visited[node] = 1
#                     heapq.heappush(q,[d+linked[v][node],node])
#         break #트리라서 한 번만 확인하면 됨.
#
# q = [[0,v]]
# visited = [0] * (n + 1)
# visited[v] = 1
# while q:
#     d,v = heapq.heappop(q)
#     for node in linked[v]:
#         if not visited[node]:
#             visited[node] = 1
#             heapq.heappush(q,[d+linked[v][node],node])
# print(d)

#deque 버전
from collections import defaultdict,deque
o = open('input.txt')
n = int(next(o))
linked = [defaultdict(int) for i in range(n+1)]
for i in o:
    info = [*map(int,i.split())]
    for i in range(1,len(info)-1,2):
        linked[info[0]][info[i]] = info[i+1]
        linked[info[i]][info[0]] = info[i+1]

q = deque([1]) #어느 지점이든 가장 먼점은 가장 끝단임.(트리 상 다 연결되어있으니까)
visited = [0] * (n + 1)
visited[1] = 1
while q:
    v = q.popleft()
    for node in linked[v]:
        if not visited[node]:
            visited[node] = visited[v] + linked[v][node]
            q.append(node)

v=visited.index(max(visited))
q = deque([v]) # 초기 점 기준 가장 먼 점에서 가장 먼 곳 연결
visited = [0] * (n + 1)
visited[v] = 1
while q:
    v = q.popleft()
    for node in linked[v]:
        if not visited[node]:
            visited[node] = visited[v] + linked[v][node]
            q.append(node)
print(max(visited)-1) #처음 거리값 고려