n, m = map(int,input().split())
graph = [[5001]*(n+1) for _ in range(n+1)] #간선 최대 개수가 5000개이니 그거보다 크게
for _ in range(m):
    x,y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1
for k in range(1,n+1): #거쳐가는 점
    for i in range(1,n+1): #시작 점
        for j in range(1,n+1): #끝 점
            if graph[i][j] > graph[i][k] + graph[k][j]: # 경유하는 것 보다 길면
                graph[i][j] = graph[i][k] + graph[k][j]
print(min(map(lambda x:(sum(graph[x]),x),range(1,n+1)))[1] )