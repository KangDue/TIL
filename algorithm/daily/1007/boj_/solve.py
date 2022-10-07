"""
기타줄
개당 가격이든, 패키지 가격이든 둘중 하나라도 가장 낮은거부터 나열하면 된다.
묶음중 제일 싼거랑
개당중 제일 싼거를 구분해야함
그래야 6개 나눈 나머지에 대해 처리 가능.
"""
import sys
sys.stdin = open('input.txt')
from collections import deque

n, m, v = map(int, input().split())

vertix = [i for i in range(n + 1)]

edge = []
for _ in range(m):
    edge.append(list(map(int, input().split())))

adj = [[] for i in range(n + 1)]

for e in edge:
    adj[e[0]].append(e[1])
    adj[e[1]].append(e[0])

for i in adj:
    i.sort()

def dfs(adj, v):
    stack, dfs_visited = list(), list()

    stack.append(v)

    while stack:
        node = stack.pop()
        if node not in dfs_visited:
            dfs_visited.append(node)
            temp = adj[node][:]
            temp.reverse()
            stack.extend(temp)
    return dfs_visited


def bfs(adj, v):
    from collections import deque
    bfs_visited = []
    queue = deque()
    queue.append(v)

    while queue:
        node = queue.popleft()
        if node not in bfs_visited:
            bfs_visited.append(node)
            queue.extend(adj[node])

    return bfs_visited


for i in dfs(adj, v):
    print(i, end=' ')

print()
for i in bfs(adj, v):
    print(i, end=' ')