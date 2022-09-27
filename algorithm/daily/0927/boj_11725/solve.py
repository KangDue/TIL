import sys
# sys.stdin = open('input.txt')
"""
트리의 부모 찾기
루트 없는 트리가 주어진다. 이떄 루트를 1이라 정하고
각 노드의 부모를 구하자.
그래프를 만들고 bfs 갈겨버리자.
"""
o = open('input.txt')
from collections import deque
n = int(next(o))
tree = [[] for _ in range(n+1)]
parent = [i for i in range(n+1)]
parent[1] = 1
visited = [0] * (n+1)
visited[1] = 1
for _ in range(n-1):
    x,y = map(int,next(o).split())
    tree[x].append(y)
    tree[y].append(x)

q = deque([1])
while q:
    now = q.popleft()
    for nv in tree[now]:
        if not visited[nv]:
            visited[nv] = 1
            parent[nv] = now
            q.append(nv)
print(*parent[2:],sep='\n')