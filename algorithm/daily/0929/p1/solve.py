import sys
sys.stdin = open('input.txt')
"""
DFS
"""
edges = [*map(int,input().split())]
graph=dict()
for i in range(0,len(edges),2):
    if graph.get(edges[i]):
        graph[edges[i]].append(edges[i+1])
    else:
        graph[edges[i]] = [edges[i + 1]]
    if graph.get(edges[i+1]):
        graph[edges[i+1]].append(edges[i])
    else:
        graph[edges[i+1]] = [edges[i]]

visited = dict()

stack = [1]
visited[1]=1
while stack:
    now = stack.pop()
    print(now,end=" ")
    for nv in graph[now]:
        if not visited.get(nv):
            stack.append(nv)
            visited[nv] = 1


