import sys
sys.stdin = open('input.txt')
"""
정점의 수, 간선의 수, 시작 점(N,M,V)
간선은 양방향.
간선 최대 10000개라서 굳이 한 번에 읽어올 필요 x
"""
from collections import deque
n,m,v = map(int,input().split())
#인접리스트 생성
graph = [[] for i in range(n+1)] #노드번호는 1~n번임
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in graph:
    if i: i.sort()
#DFS
stack = []
svisited = [0] * (n+1)
stack.append(v)
shist = []
while stack:
    now = stack.pop()
    if svisited[now]: continue
    shist.append(now)
    svisited[now] = 1 #방문처리를 여기서 해줘야 그 노드에 연결된 노드를 먼저 방문함.
    for node in graph[now][::-1]:
        if svisited[node] == 0 :#간 적 없는 것만 추가
            stack.append(node)

q = deque([v])
qvisited = [0] * (n+1)
qvisited[v] = 1
qhist = []
while q:
    now = q.popleft()
    qhist.append(now)
    for node in graph[now]:
        if qvisited[node] == 0:
            q.append(node)
            qvisited[node] = 1
print(*shist)
print(*qhist)