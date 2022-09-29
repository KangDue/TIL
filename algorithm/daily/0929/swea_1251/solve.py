import sys
sys.stdin = open('input.txt')
"""
하나로
N개의 섬들을 연결하자.
모든 섬을 해저터널로 연결하는데 
환경부담금 = 부담세율(E) * 터널길이(L)^2
그냥 MST 문제
거리는 진짜 좌표상 거리 (어떤 거리인지는 안주어졌지만 그냥하자 일단 유클리디안)
#prim으로 하자
"""
INF = int(1e12)
def prim(start):
    val = {i:INF for i in graph}
    visited = {i:0 for i in graph}
    val[start] = 0
    for _ in graph:
        mindex = -1
        minv = INF
        for i in graph:
            if not visited[i] and val[i] < minv:
                mindex = i #어차피 좌표로 변경할거라 상관 x
                minv = val[i]
        visited[mindex] = 1
        for nv,co in graph.get(mindex,[]):
            if not visited[nv] and val[nv] > co:
                val[nv] = co
    return round(sum(val.values())*E)

eud = lambda x,y:(x[1]-y[1])*(x[1]-y[1]) + (x[0]-y[0])*(x[0]-y[0])
for t in range(int(input())):
    n = int(input())
    graph = dict()
    xs = [*map(int,input().split())]
    ys = [*map(int,input().split())]
    for i in range(n):
        graph[(xs[i],ys[i])] = []
    E = float(input())
    for i in graph:
        for j in graph:
            if i!=j:
                graph[i].append([j,eud(i,j)])
    ans = prim((xs[0],ys[0]))
    print(f'#{t+1} {ans}')


