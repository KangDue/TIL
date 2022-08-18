import sys
sys.stdin = open('input.txt',encoding='utf-8')
# DFS
# 정점의 수, 간선의 수
# 2개씩 간선 주어짐
for t in range(1):
    n, e = map(int,input().split())
    edges = list(map(int,input().split()))
    graph = {i:[] for i in range(1,n+1)}
    for i in range(0,e<<1,2): # 간선 * 2 해야함
        graph[edges[i]].append(edges[i+1])
        graph[edges[i+1]].append(edges[i])
    v = 1 #시작점
    stack = [v]
    hist = []
    while stack:
        v = stack.pop()
        if v not in hist: #간적 없는놈만 추가
            hist.append(v)
        for i in reversed(graph[v]): # 간적 없는 놈 추가
            if i not in hist: #둘다에 없어야 중복없이 나온다.
                stack.append(i)
    print(hist)


