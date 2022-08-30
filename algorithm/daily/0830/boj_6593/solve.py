import sys
sys.stdin = open('input.txt')
"""
상범빌딩
당신이 빌딩에 갇혀있는데 탈출하는 가장 빠른길은?
동서남북상하 6방향으로 1분에 한칸씩 이동가능
각 정육면체는 금으로 이루어져있고 지나갈 수 없거나 비어있어서 지나갈 수 있다.
(토마토 3d버전이랑 비슷한듯)
벽 = #, 길 = . , 시작 = S, 탈출 E
각 층 사이에는 빈 줄이 있으며, 입력의 끝은 L,R,C가 모두 0 으로 표현된다.
즉 0,0,0 입력 받으면 끝.
"""
from collections import deque
to = [[0,1,0],[0,-1,0],[0,0,-1],[0,0,1],[1,0,0],[-1,0,0]]#6방향
while 1: #어차피 0층이거나 0행이거나 0열일 수 없어서 and도 괜찮지만 혹시모르니 or가자
    L, R, C = map(int, input().split())
    if not(L and R and C) : break
    build = [[[] for _ in range(R)] for _ in range(L)]
    for h in range(L):
        for y in range(R):
            build[h][y] = [*input()]
        input()
    visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    find = 0
    try:
        for h in range(L):
            for i in range(R):
                for j in range(C):
                    if build[h][i][j] == 'S':
                        sh,sy,sx = h,i,j; find += 1
                    if build[h][i][j] == 'E':
                        eh,ey,ex = h,i,j; find += 1
                if find == 2:
                    raise Exception
    except: pass

    q = deque([[sh,sy,sx,0]]) #탈출 시간 측정
    visited[sh][sy][sx] = 1
    while q:
        try:
            h,y,x,time = q.popleft()
            for dh,dy,dx in to:
                nh = h+dh; ny = y + dy; nx = x +dx
                if 0<=nh<L and 0<=ny<R and 0<= nx < C\
                        and visited[nh][ny][nx] == 0 and build[nh][ny][nx] != '#':
                    q.append([nh,ny,nx,time+1])
                    visited[nh][ny][nx] = 1
                    if (nh,ny,nx) == (eh,ey,ex):
                        print(f'Escaped in {time+1} minute(s).')
                        raise Exception
        except:break
    else: print('Trapped!')





