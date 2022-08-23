import sys
sys.stdin = open('input.txt', encoding='utf-8')

for t in range(1,11):
    tc, n = map(int,input().split())
    edges = list(map(int,input().split()))
    graph = {i:[] for i in range(100)}
    for i in range(0,n*2,2):
        graph[edges[i]].append(edges[i+1]) # 방향성 그래프
    #stack구현
    hist, stack = [],[0]
    while stack:
        v = stack.pop()
        if v not in hist:
            hist.append(v)
        for i in graph[v]:
            if i not in hist:
                stack.append(i)
    #판별
    if 99 in hist: #  경로가 있으면
        print(f'#{t} 1')
    else: #경로가 없으면
        print(f'#{t} 0')