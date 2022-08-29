import sys
sys.stdin = open('input.txt')
"""
지훈이 미로 탈출 돕기
- 지훈이의 위치와 불이붙은 위치를 감안해서
지훈이가 불에 타기전에 탈출 할 수 있는지?
있다면 얼마나 빨리 탈출 할 수 있는지?
지훈이와 불은 매 분마다 상하좌우로 이동한다
불은 4방향으로 확산한다.
지훈이는 미로의 가장자리에 접한 공간에서 탈출 할  수 있다.
지훈이와 불은 벽은 못지나 간다.
"""
from collections import deque
R,C = map(int,input().split())
# #벽, . 길, J 지훈이 초기위치, F:불이난 공간
# J는 유일하고, F는 여러개일 수 있음
maze = [[*input()] for _ in range(R)]
fire=[]
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            J = [i,j,0] #좌표와 시간
        if maze[i][j] == 'F':
            fire.append([i,j,0]) #불은 시간을 누적할 필요가 있을까?? 없긴한데 지훈이랑 한꺼번에 돌릴거니까 필요

visited = [[0 for _ in range(C)] for _ in range(R)]
q = deque(fire)
q.append(J)
for y,x,z in fire:
    visited[y][x] = 1 #방문처리
visited[J[0]][J[1]] = 1 #방문처리

to = [[1,0],[-1,0],[0,1],[0,-1]]
while q:
    y, x, time = q.popleft()
    #아래서 R-1, C-1 이 인덱스범위다
    if (y == 0 or y == R-1 or x == 0 or x == C-1) and maze[y][x] == 'J':  # pop 바로 다음에 확인하면 현재노드가 확인이 안됨.
        print(time+1)#시작위치 시간을 포함한다.
        break
    if maze[y][x] == 'J': #지훈이 이동.
        for dy,dx in to:#불이 각 지점에서 4방향으로 퍼지는걸 고려 안했다 ....
            ny = y+dy; nx = x+dx
            if 0<=ny<R and 0<= nx < C and maze[ny][nx] != '#' and visited[ny][nx] == 0:
                maze[ny][nx] = 'J'
                maze[y][x] = '.' #지나가면 길임`
                visited[ny][nx] = 1
                q.append([ny,nx,time+1])
    if maze[y][x] == 'F':
        for dy,dx in to:#불이 각 지점에서 4방향으로 퍼지는걸 고려 안했다 ....
            ny = y+dy; nx = x+dx
            if 0<=ny<R and 0<= nx < C and maze[ny][nx] != '#':
                if visited[ny][nx] == 0:
                    maze[ny][nx] = 'F' #지나가면 길임
                    visited[ny][nx] = 1
                    q.append([ny,nx,time+1])
else: #도착을 못하면
    print('IMPOSSIBLE')
#마지막에 print()넣어놔서 자꾸 틀림 ;