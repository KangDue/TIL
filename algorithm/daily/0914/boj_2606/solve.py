import sys
sys.stdin = open('input.txt')
"""
바이러스 감염!
간단한 그래프 탐색 - 연결여부 확인문제
"""
from collections import deque
n = int(input())
e = int(input())
graph = [[] for i in range(n+1)]
for i in range(e):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [0]*(n+1)
q = deque([1])
visited[1] = 1
while q:
    v = q.popleft()
    for l in graph[v]:
        if visited[l] == 0:
            q.append(l)
            visited[l] = 1
print(sum(visited)-1)
