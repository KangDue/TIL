import sys
sys.stdin = open('input.txt',encoding='utf-8')

for t in range(1,int(input())+1):
    v,e = map(int,input().split())#노드(1~ v)와 간선의 수
    graph = {i:[] for i in range(1,v+1)}
    for i in range(e):
        x,y = map(int,input().split())
        graph[x].append(y) # 방향성 그래프
    start,end = map(int,input().split())
    #stack구현
    hist, stack = [],[start]
    while stack:
        v = stack.pop()
        if v not in hist:
            hist.append(v)
        for i in graph[v]:
            if i not in hist:
                stack.append(i)
    #판별
    if end in hist: #  경로가 있으면
        print(f'#{t} 1')
    else: #경로가 없으면
        print(f'#{t} 0')