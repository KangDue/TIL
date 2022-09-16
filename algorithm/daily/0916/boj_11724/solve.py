import sys
sys.stdin = open('input.txt')
"""
무방향 그래프의 연결요소 개수 구하기
영역 구하기 문제와 비슷한듯.
하나로 연결된 부분의 개수 구하는 것
"""
import sys
from collections import deque
input = sys.stdin.readline
n,m=map(int,input().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [0]*(n+1)
count = 0
for i in range(1,n+1):
    if not visited[i]:
        count += 1
        q = deque([i])
        visited[i] = 1
        while q:
            v = q.popleft()
            for nv in graph[v]:
                if not visited[nv]:
                    visited[nv]=1
                    q.append(nv)
print(count)
