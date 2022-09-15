import sys
sys.stdin = open('input.txt')
from collections import deque
for t in range(10):
    l,v = map(int,input().split())
    visited = [0]*101
    graph = [[] for i in range(101)]
    flag = 0
    for i in map(int,input().split()):
        flag ^= 1
        if flag:a=i
        else:graph[a].append(i)
    q = deque([v])
    visited[v]=1
    while q:
        now = q.popleft()
        for e in graph[now]:
            if not visited[e]:
                visited[e]=visited[now]+1
                q.append(e)
    for i in range(100,0,-1):
        if visited[i]==visited[now]:print(f'#{t+1} {i}');break
