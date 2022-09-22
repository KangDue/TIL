import sys
sys.stdin = open('input.txt')
"""
특정한 최단경로
무방향 그래프에서 1 -> N 정점으로 최단거리 이동
1. 임의의 두 정점 반드시 통과해야함.
p2. 갔던길을 또 갈 수 있지만 반드시 최단거리 여야 한다.
#전형적인 다익스트라 ?
N = 800, E = 200000 상한선

이 문제처럼 순환도 가능하면서 특정 경로를 거쳐야 하는 문제들은
다익스트라 한번으로는 안풀림. 각 경로에 대해서 실행해주어야함.
그리고 if 문으로 거리에 대한 filter링이 없으면 답은 나오지만 memory 초과뜨기 쉬움
거리가 짧아질때만 넣어주자.

"""
import heapq
o = open('input.txt')
n,e = map(int,next(o).split())
graph = [dict() for i in range(n+1)]
for _ in range(e):
    x,y,z = map(int,next(o).split())
    graph[x][y] = z
    graph[y][x] = z

v1,v2 = map(int,next(o).split())
other = {v1:v2, v2:v1}
ans = [] # 1에서 v1,v2까지 최단거리
for x1 in (v1,v2):
    q = [[0,1]]
    dist = [1e+9]*(n+1)
    dist[1] = 0
    while q:
        d,now = heapq.heappop(q)
        if now == x1:
            ans.append(d)
            break
        for nv in graph[now]:
            cost = d+graph[now][nv]
            if dist[nv] > cost:
                dist[nv] = cost
                heapq.heappush(q,[cost,nv])
    else:ans.append(0)


ans2 = [] # v1에서 v2까지, v1 에서 v2까지 최단거리
for x1 in (v1,v2):
    q = [[0,x1]]
    dist = [1e+9]*(n+1)
    dist[x1] = 0
    while q:
        d,now = heapq.heappop(q)
        if now == other[x1]:
            ans2.append(d)
            break
        for nv in graph[now]:
            cost = d+graph[now][nv]
            if dist[nv] > cost:
                dist[nv] = cost
                heapq.heappush(q,[cost,nv])
    else: ans2.append(0)


ans3 = []
for x1 in (v1,v2):
    q = [[0,other[x1]]]
    dist = [1e+9]*(n+1)
    dist[other[x1]] = 0
    while q:
        d,now = heapq.heappop(q)
        if now == n:
            ans3.append(d)
            break
        for nv in graph[now]:
            cost = d+graph[now][nv]
            if dist[nv] > cost:
                dist[nv] = cost
                heapq.heappush(q,[cost,nv])
    else: ans3.append(0)
if (ans[0] and ans2[0] and ans3[0]) or (ans[1] and ans2[1] and ans3[1]):
    print(min(ans[0]+ans2[0]+ans3[0],ans[1]+ans2[1]+ans3[1]))
else: print(-1)

# print(*dist,sep='\n')
# print('graph',graph)
# print('dist',dist)