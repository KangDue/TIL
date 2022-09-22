import sys
sys.stdin = open('input.txt')
"""
토마토 p2 (3D버전)
토마토를 보관하는 큰 창고를 가지고 있다.
MxNxH상자에 담겨있다.
하루가 지나면 익은 토마토 옆 설익은 것들이 익는다.(전파)(상하좌우위아래)
며칠이 지나면 모두 익는지 최소 일수를 구하시오.
모든 토마토가 익으면 0, 익지 못하면 -1, 첨부터 전부 익어있다면? 1
토마토 = 1, 안 익은 토마토 = 0, 없으면 -1
매 시간마다 토마토가 익어있는 상태를 전파 하니까 time과 같이 bfs를 돌리자
채우는 값도 같이 바꿔줘야 시간을 알기 편함.
"""
from collections import deque
C,R,H = map(int,input().split())
tomato = [[[*map(int,input().split())] for _ in range(R)] for _ in range(H)]
st = sum(sum(tomato,start=[]),start=[]) # 1행으로 펴기
if 0 in st:#처음부터 다 익은 상태가 아니면
    #3차원 indexing은 H,R,C로 해야함.
    #3차원이라고 별꺼 있나 ? 마 해보자!
    visited =[[[0 for _ in range(C)] for _ in range(R)] for _ in range(H)]
    to = [[0,1,0],[0,-1,0],[0,0,1],[0,0,-1],[1,0,0],[-1,0,0]]#상하좌우앞뒤/순서가 맞진 않음.
    #모든 익은 토마토들이 0인 상태로 시작해야 한다.
    tos = []
    for k in range(H):
        for i in range(R):
            for j in range(C):
                if tomato[k][i][j] == 1:
                    tos.append([k,i,j,0])
    q = deque(tos)
    for h,r,c,time in tos:
        visited[h][r][c] = 1
    while q:
        h,y,x,time = q.popleft()
        for dh,dy,dx in to:
            nh = h+dh ; ny = y+dy; nx = x + dx
            if 0<= nh < H and 0<= ny < R and 0<= nx < C\
                and visited[nh][ny][nx] == 0 and tomato[nh][ny][nx] == 0:
                #유효범위, 방문x, 설익은놈일때
                q.append([nh,ny,nx,time+1])
                visited[nh][ny][nx]=1
                tomato[nh][ny][nx] = time + 1
    nt = sum(sum(tomato,start=[]),start=[]) # 1행으로 펴기
    if 0 in nt: print(-1) #모두 익지 못하면
    else: print(max(nt)) #모두 익었다면 다 익는데 걸린 시간
else:#처음부터 다 익은 상태
    print(0)