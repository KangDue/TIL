import sys
sys.stdin = open('input.txt')
"""
토마토를 보관하는 큰 창고를 가지고 있다.
MxN상자에 담겨있다.
하루가 지나면 익은 토마토 옆 설익은 것들이 익는다.(전파)(상하좌우)
며칠이 지나면 모두 익는지 최소 일수를 구하시오.
모든 토마토가 익으면 0, 익지 못하면 -1, 첨부터 전부 익어있다면? 1
토마토 = 1, 안 익은 토마토 = 0, 없으면 -1
"""
from collections import deque
C,R = map(int,input().split()) #보통 R,C로 주는데 반대임을 유의
tomato = [[*map(int,input().split())] for i in range(R)]
checkto = sum(tomato,start=[])
if checkto.count(0):#안익은게 있다면 정상시행
    visited = [[0 for _ in range(C)] for _ in range(R)]
    #어떻게 확산시킬까?
    # 1인 녀석들만 좌표를 따서 한번에 bfs를 진행시켜 볼까? ㅇㅋ
    start = []
    for i in range(R):
        for j in range(C):
            if tomato[i][j]==1:#익은 토마토면
                start.append([i,j,0]) #좌표와 시간
    q = deque(start)#한꺼번에 넣어놓기
    #일단 첫값은 visited 처리
    for y,x,z in start:
        visited[y][x] = 1
    to = [[1,0],[-1,0],[0,1],[0,-1]]
    while q:
        y,x,time = q.popleft()
        for dy,dx in to:
            ny = y+dy; nx = x+dx
            if 0<= ny < R and 0<= nx < C and visited[ny][nx] == 0 and tomato[ny][nx] == 0:
                q.append([ny,nx,time+1])
                visited[ny][nx] = 1
                tomato[ny][nx] = time+1#설익은 녀석 전파
    tomato = sum(tomato,start=[])
    cant = tomato.count(0)
    if cant:print(-1)
    else:print(max(tomato))
else:
    print(0)
