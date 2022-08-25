import sys
sys.stdin = open('input.txt')
def DFS(y,x):
    global path, paths, maze
    temp = []
    for b,a in di:
        yy = y+b; xx = x + a
        if maze[yy][xx] != '1' and visited[yy][xx] == 0:
            temp.append((yy,xx))
    if not temp:#주변 전부 방문했다면 끝점
        paths.append(path[:])
    else:
        for row,col in temp:
            visited[row][col]=1
            path.append((row,col))
            DFS(row,col)
            path.pop()
            visited[row][col]=0

# def DFS(y,x):
#     global path, paths, maze
#     end = True
#     for b, a in di:
#         yy = y + b; xx = x + a
#         if visited[yy][xx] == 0:
#             end = False
#             break
#     temp = []
#     for b,a in di:
#         yy = y+b; xx = x + a
#         if maze[yy][xx] != '1' and visited[yy][xx] == 0:
#             temp.append((yy,xx))
#     if end:#주변 전부 방문했다면 끝점
#         paths.append(path[:])
#     else:
#         for b,a in di:
#             yy = y+b; xx = x + a
#             if maze[yy][xx] != '1' and visited[yy][xx] == 0:
#                 visited[yy][xx]=1
#                 path.append((yy,xx))
#                 DFS(yy,xx)
#                 path.pop()
#                 visited[yy][xx]=0

#모든경로 기록하는 버전
d,w,r=int,input,range
for t in r(d(w())):
    n=d(w())
    maze=['1'*(n+2)]+['1'+w()+'1' for i in r(n)]+['1'*(n+2)]
    visited = [[0]*(n+2) for i in range(n+2)]
    for i in range(n+2):
        for j in range(n+2):
            if maze[i][j] == '1':
                visited[i][j] = 1
    for y in r(n+2):
        x=maze[y].find('2')
        z=maze[y].find('3')
        if x > -1:s=[y,x]#출발지 찾기
        if z > -1:e=(y,z)  #도착지 찾기
    di=[[1,0],[-1,0],[0,1],[0,-1]]
    visited[s[0]][s[1]] = 1
    path=[]
    paths=[]
    #print(f'#{t+1} {ans}')
    DFS(s[0],s[1])
    print(*paths,sep='\n')






from collections import deque,defaultdict as df
d,w,r=int,input,range
for t in r(d(w())):
    n=d(w())
    maze=['1'*(n+2)]+['1'+w()+'1' for i in r(n)]+['1'*(n+2)]
    for y in r(n+2):
        x=maze[y].find('2')
        z=maze[y].find('3')
        if x > -1:s=[y,x,0]#출발지 찾기
        if z > -1:e=(y,z)  # 출발지 찾기
    q=deque([s])
    hist=df(d)
    di=[[1,0],[-1,0],[0,1],[0,-1]]
    while len(q):
        pos=q.popleft()
        for row,col in di:
            y,x=pos[0]+row,pos[1]+col
            if maze[y][x] != '1' and (y,x) not in hist:
                q.append([y,x,pos[2]+1])
                hist[(y,x)] = pos[2]+1
    if hist[e]:ans=hist[e]-1
    else:ans=0
    print(f'#{t+1} {ans}')





