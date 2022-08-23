from collections import defaultdict as dd
def dfs(here):
    global visited, graph
    print(here)
    if visited[here]: # 방문한적 있으면
        if visited[here] == -1:
            return True
        return False #

    visited[here] = -1 #방문한적 없으면 -1
    for node in graph[here]: #연결된 각 노드를 순회하며
        if dfs(node):
            return True #-1을 다시 만나면 순환이 존재한다는 뜻

    visited[here] = 1
    return False

def solution():
    global visited, graph
    n = 7
    edges = [(1,2), (1,5), (2,3), (2,6), (3,4), (6,4), (4,7), (7,6)]
    graph = dd(list)
    for edge in edges:
        v,w = edge
        graph[v].append(w)
    visited = [0]*(n+1) #node별 방문정보 저장
    return dfs(2) # 2가 시작노드

solution()



