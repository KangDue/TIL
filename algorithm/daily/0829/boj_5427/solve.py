import sys
sys.stdin = open('input.txt')
"""
초반에 비슷한 문제가 있었다.
<불>
매 초마다, 불은 동서남북 방향으로 인접한 빈 공간으로 퍼져나간다. 
1. 벽에는 불이 붙지 않는다. 상근이는 동서남북 인접한 칸으로 이동할 수 있으며, 1초가 걸린다.
p2. 상근이는 벽을 통과할 수 없고, 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없다.
3. 상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다.

상근이를 큐에 먼저 넣어줘야 불이 번짐과 동시에 이동하는 것과 같음.
빌딩의 지도가 주어졌을 때, 얼마나 빨리 빌딩을 탈출할 수 있는지 구하는 프로그램을 작성하시오.
. 길, # 벽 , @ 상근이, * 불
탈출지점: 테두리

!!!!!!
불은 "동시"에 번진다.

"""
from collections import deque
for t in range(int(input())):
    C,R = map(int,input().split())
    buil = [[*input()] for _ in range(R)]
    visited = [[0 for _ in range(C)] for _ in range(R)]
    fvisited = [[0 for _ in range(C)] for _ in range(R)]
    fire = []
    for i in range(R):
        for j in range(C):
            if buil[i][j] == '@':
                sy,sx = i,j
                visited[i][j] = 1
            if buil[i][j] == '*':
                fire.append([i,j,0])
                fvisited[i][j] = 1
    q = deque([[sy,sx,0]]+fire) #불이 붙으려는 칸으로 갈 수 없는데, = 와버렸다? 태우면 됨.
    to = [[1,0],[-1,0],[0,1],[0,-1]]
    while q:
        y,x,time = q.popleft()
        if (y==0 or y==R-1 or x == 0 or x==C-1) and buil[y][x]=='@':
            print(time+1);break #문 도착해서 나가는 시간 +1

        if buil[y][x] == '*':
            for dy, dx in to:
                ny = y+dy; nx = x+dx
                if 0<=ny<R and 0<=nx<C and buil[ny][nx] != '#' and fvisited[ny][nx] == 0:
                    buil[ny][nx] = '*'
                    q.append([ny,nx,time+1])
                    fvisited[ny][nx] = 1 #visited를 따로 쓴다.

        else:#상근이
            for dy,dx in to:
                ny = y+dy; nx = x+dx
                if 0<=ny<R and 0<=nx<C and buil[ny][nx] != '#':
                    if buil[ny][nx] == '.' and visited[ny][nx] == 0:#상근이고 다음이 길일때만 가능
                        buil[ny][nx] = '@'
                        q.append([ny, nx, time + 1])
                        visited[ny][nx] = 1
    else:#탈출 불가
        print("IMPOSSIBLE")
    # print(*buil,sep='\n')
    # print(*visited, sep='\n')