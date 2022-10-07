"""
여행 가자
중복으로 여행이 가능한 어떤 경로가 주어지는데
여행지간의 연결 관계가 주어질 때
이 경로가 정말로 실행 가능한 지?
disjoint set 으로 해결 가능해보이지만
질문게시판 질문이 bfs니 bfs로 풀어주자!
80%에서 틀렸는데 단순히 set으로 하나인지 볼께 아니라 서로가 순서에 맞게 연결 상태인지 확인하는게 맞음.
"""

import sys
sys.stdin = open('input.txt')
from sys import stdin

input = stdin.readline
from collections import deque

N = int(input())
M = int(input())

graphs = [[] for i in range(N + 1)]

for i in range(1, N + 1):
    for ind, j in enumerate(map(int, input().split())):
        if j == 1:
            graphs[i].append(ind + 1)

plan = list(map(int, input().split()))
def bfs(i, j):
    """ if i -> j : True else False"""
    q = deque()
    visited = [False] * (N + 1)
    q.append(i)

    while q:
        x = q.popleft()
        visited[x] = True

        for nx in graphs[x]:
            if nx == j:
                return True
            else:
                if not visited[nx]: q.append(nx)

    return False


Flag = False
for i in range(len(plan) - 1):
    comb = (plan[i], plan[i + 1])
    comb2 = (plan[i + 1], plan[i])
    if not bfs(*comb): Flag = True
    if not bfs(*comb2): Flag = True; break

if Flag:
    print("NO")
else:
    print("YES")
#
# from collections import deque
# import sys
# input = sys.stdin.readline
# n = int(input())
# m = int(input())
# #인접행렬로 주어짐
# grid = [[*map(int,input().split())] for _ in range(n)]
# plan = [*map(int,input().split())]
# graph = [[] for _ in range(n+1)]
# if m:
#     for i in range(n):
#         for j in range(i,n):
#             if grid[i][j]:
#                 graph[i+1].append(j+1)
#                 graph[j+1].append(i+1)
#
#     count = 1
#     for start in range(m-1):
#         if plan[start] == plan[start+1]: #같은 경로 연속으로 나오는 경우가 있음.
#             count += 1
#             continue
#         q = deque([plan[start]])
#         visited = [0]*(n+1)
#         visited[plan[start]] = 1
#         while q:
#             try:
#                 now = q.popleft()
#                 for nv in graph[now]:
#                     if not visited[nv]:
#                         visited[nv] = 1
#                         q.append(nv)
#                         if nv == plan[start+1]:
#                             count += 1
#                             raise Exception
#             except:
#                 break
#     if count == m:
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("YES")