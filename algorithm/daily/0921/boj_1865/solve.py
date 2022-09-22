import sys
# sys.stdin = open('input.txt')
"""
웜홀
N개의 지점, M개의 도로 , W개의 웜홀 (각 제한 500, 2500,200)
도로는 무방향, 웜홀은 방향
웜홀 = 시작위치에서 도착위치로 가는 하나의 경로(특이하게 시간이 뒤로가게됨)
한지점에서 출발하여 웜홀을 타고 다시 출발점으로 돌아올때
출발할때 과거로 가는게 가능한가? YES or NO
- 벨만포드로 풀어야하는거 같은데 , 아직 모르니 다익스트라 노가다 하자
"""
# 1. 벨만포드 버전
# o = open('input.txt')
# for t in range(int(next(o))):
#     n,m,w = map(int,next(o).split())
#     graph = [[] for _ in range(n+1)]
#     # graph = [[1e+9] * (n + 1) for _ in range(n + 1)]
#     for _ in range(m):
#         x,y,z = map(int,next(o).split())
#         graph[x].append((y,z))
#         graph[y].append((x,z))
#         # graph[x][y] = z
#         # graph[y][x] = z
#
#     for _ in range(w): #음의 간선
#         x,y,z = map(int,next(o).split())
#         graph[x].append((y,-z))
#         #여기서 y가 도착점임.
#
#     ans = 'NO'                 #모든 점이 연결되어 있다면 아무거나 1개만 해도 됨.
#     for start in range(1,n+1): #독립 되어있을 수 도 있기에 하나만 보면 안됨.
#         if not graph[start]: continue #start 찾는건 좋은데 찾고나면 끝내야지
#         try:
#             dist = dict()
#             for node in range(1,n+1):
#                 dist[node] = int(1e+9)
#             dist[start]=0
#             for i in range(n):
#                 for j in range(1,n+1):
#                     for nv,co in graph[j]:
#                         if dist[nv] > dist[j] + co:
#                             dist[nv] = dist[j] + co
#                             if i==n-1: ans = 'YES'; raise Exception
#         except:
#             break
#         break
#     print(ans)



# p2. 플로이드 워셜 버전
# c++ 플로이드 워셜로 푼사람 본 결과 c++로도 python 벨만포드 속도가 나옴.
# 94% 채점중 시간초과 뜸
# 같은 간선이 가중치만 다른게 있어서 아래처럼 조건을 달고 값을 안받아오면
# 플로이드로 풀었을때 78프로인가에서 짤림.
# 근데 왜 위의 벨만포드에서는 풀리냐?? 약간의 운인듯 ㅇㅇ 인줄 알았지만,
## 워셔는 값을 받아오면 덮어쓰는데 벨만포드는 추가하는 방식이라 다른듯
# 왜냐하면 음의 간선이 있더라도 사이클상 양의 가중치가 더 크다면 음의 순환은 안생김.
# o = open('input.txt')
# for t in range(int(next(o))):
#     n,m,w = map(int,next(o).split())
#     # graph = [[] for _ in range(n+1)]
#     graph = [[1e+9] * (n + 1) for _ in range(n + 1)]
#     for i in range(1,n+1):
#         graph[i][i] = 0
# 
#     for _ in range(m):
#         x,y,z = map(int,next(o).split())
#         if graph[x][y] > z: #여기!
#             graph[x][y] = z
#             graph[y][x] = z
#     for _ in range(w): #음의 간선
#         x,y,z = map(int,next(o).split())
#         if graph[x][y] > -z: #여기!
#             graph[x][y]=-z
# 
#     #웜홀까지 가는 최단경로 찾기.출발점에서 웜홀을 안거치는 도착점까지 최단경로 찾기
#     for k in range(1,n+1):
#         for i in range(1,n+1):
#             for j in range(1,n+1):
#                 graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
#     #시간이 줄어들면서 ...?
#     #무조건 음수가 아니라 줄기만 하면 된다.
#     for i in range(1,n+1):
#         if graph[i][i]<0:
#             print('YES')
#             break
#     else:
#         print('NO')
#     print(*graph,sep='\n')


# 3. 벨만포드 버전2
o = open('input.txt')
inp = lambda x:next(x).split() #람다로 저장해서 호출하면 이쁘긴한데, 느려짐. 조금
for t in range(int(next(o))):
    n,m,w = map(int,inp(o))
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        x,y,z = map(int,inp(o))
        graph[x].append((y,z))
        graph[y].append((x,z))
    for _ in range(w): #음의 간선
        x,y,z = map(int,inp(o))
        graph[x].append((y,-z))
    ans = 'NO'
    try:
        dist = dict()
        for node in range(1,n+1):
            dist[node] = 1e+9
        #따라서 V + E임.
        for i in range(n): #거쳐가는 점.
            for j in range(1,n+1): #아래 for와 함께 모든 edge 확인하는 문장임.
                for nv,co in graph[j]:
                    if dist[nv] > dist[j] + co:
                        dist[nv] = dist[j] + co
                        if i==n-1: ans = 'YES';raise Exception
    except: pass
# dist[start]=0 애초의 음의간선 판별기로 만들어져서 시작점 초기화 필요 x
# start에 대한 최단거리로 만들려면 dist[cur] != INF와 같은 조건 필요.
    print(ans)