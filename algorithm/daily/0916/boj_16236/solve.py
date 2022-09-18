import sys
sys.stdin = open('input.txt')
"""
NxN공간 물고기 M마리 , 아기 상어 1마리
한칸에 최대 물고기 1마리
상어 물고기 모두 각자의 크기가 있고
상어는 자기보다 큰 물고기 못지나침(못먹음)
크기가 같으면 지나는 가지만 못먹음
- 더 이상 먹을 고기가 없다 = mom call = 탐색이 종료되었다.
- 남은 고기 1마리면 바로 ㄱㄱ(그냥 1step씩)
- 1마리보다 가까우면 최단거리로
- 거리가 가까운게 여러마리면 가장 위, 가장 왼쪽부터 = 방향탐색 우선순위 상 좌 하 우 순으로 가자!
- 이동은 1초, 먹는데 시간 소모 x 먹으면 빈칸됨.
- 자기 크기랑 같은 수의 물고기를 먹으면 크기 1 증가
- 몇초동안 엄마를 안부르고 고기를 먹을수 있나 ?

-처음크기 = 2, 상하좌우로 1칸씩 이동가능.
-단순 bfs라기보단 물고기 좌표를 알아야하니 조합같음 - 못지나가는 경로 판단이 안됨. - bfs 가자
-물고기를 하나 먹을때 마다 visited를 초기화 해보자.
"""
# from collections import deque
# n = int(input())
#
# #물고기크기는 1~6, 9는 아기상어 위치
# grid = [[*map(int,input().split())] for _ in range(n)]
# fishes = dict()#물고기 정보 받아오기
# for r in range(n):
#     for c in range(n):
#         if grid[r][c] == 9: shark=[r,c,2,0,0];grid[r][c]=0 #좌표1,좌표2, 크기, 먹은수, 시간
#         elif grid[r][c]: fishes[(r,c)]=grid[r][c]
#
# to = [[-1,0],[0,-1],[0,1],[1,0]]#상 좌 우 하
# visited = [[0 for _ in range(n)] for _ in range(n)]
# visited[shark[0]][shark[1]] = 1
# q = deque([shark])
# time = 0
# while q:
#     try:
#         y,x,s,e,t = q.popleft()
#         for dy,dx in to:
#             ny = y+dy; nx = x+dx
#             if 0<=ny<n and 0<=nx<n and not visited[ny][nx]:
#                 if 0< grid[ny][nx] <s:#0보단 크고 크기보다 작으면 먹을 수 있다.
#                     print(f'ny = {ny} , nx = {nx}, value = {grid[ny][nx]} and size = {s}')
#                     grid[ny][nx] = 0
#                     visited = [[0 for _ in range(n)] for _ in range(n)]
#                     visited[ny][nx] = 1
#                     time = t+1
#                     if e+1 == s: # 크기 커짐
#                         q=deque([[ny,nx,s+1,0,t+1]])
#                     else:
#                         q=deque([[ny, nx, s, e+1, t + 1]])
#                     raise Exception
#                 elif grid[ny][nx] == s or grid[ny][nx]==0: #크기가 같으면 지나는 갈 수 있다.
#                     visited[ny][nx] = 1
#                     q.append([ny,nx,s,e,t+1])
#     except: continue
# print(*grid,sep='\n')
# # print(t)#먹고나서 움직이는 시간이 카운트됨..
# print(time,t)
from functools import reduce
# print(path)
# dist = lambda x,y: abs(x[0]-y[0])+abs(x[1]-y[1])
# ans = 0
# for i in range(len(path)-1):
#     ans+=dist(path[i],path[i+1])
# print(ans)

"""---------------------------------------------------------"""
#How to 피라미드 search ?
#아래처럼 피라미드 탐색을 하면 돌아가지 않고 그냥 훓어버림.
# def pyserch(r,c,s,e,t,step):#t초뒤 피라미드 탐색
#     global time,grid,n
#     if step == 2*n-1: return 0
#     ub = r-t if r-t >= 0 else 0
#     lb = r+t if r+t <n else n-1
#     for i in range(ub,lb+1):
#         d = t-abs(i-r) #좌우 거리
#         if d == 0:
#             if 0 < grid[i][c] < s:#먹을수 있는 칸.
#                 print(t, e, step, "---", i, c,"그리드",grid[i][c],s)
#                 grid[i][c] = 0
#                 time += t
#                 if e + 1 == s:  # 크기 커짐
#                     return pyserch(i, c, s+1, 0, 1, 1)
#                 else:
#                     return pyserch(i, c, s, e+1, 1, 1)
#         else: #양 옆 탐색
#             left = c-d
#             right = c + d
#             for j in (left,right):
#                 if 0<=j<n and 0 < grid[i][j] < s:  # 먹을수 있는 칸.
#                     print(t, e, step, "---", i, j,"그리드",grid[i][j],s)
#                     grid[i][j] = 0
#                     time += t
#                     if e + 1 == s:  # 크기 커짐
#                         return pyserch(i, j, s+1, 0, 1, 1)
#                     else:
#                         return pyserch(i, j, s, e + 1, 1, 1)
#     return pyserch(r, c, s, e, t + 1, step+1)
#
# from collections import deque
# n = int(input())
#
# #물고기크기는 1~6, 9는 아기상어 위치
# grid = [[*map(int,input().split())] for _ in range(n)]
# fishes = dict()#물고기 정보 받아오기
# for r in range(n):
#     for c in range(n):
#         if grid[r][c] == 9: shark=[r,c,2,0,0];grid[r][c]=0 #좌표1,좌표2, 크기, 먹은수, 시간
#         elif grid[r][c]: fishes[(r,c)]=grid[r][c]
#
# to = [[-1,0],[0,-1],[0,1],[1,0]]#상 좌 우 하
# grid[shark[0]][shark[1]] = 0
# q = deque([shark])
# time = 0
# pyserch(shark[0],shark[1],2,0,1,1)#r,c,s,e,t,step
# print(*grid,sep='\n')
# print(time)

"""---------------------------------------------------------"""
from collections import deque
n = int(input())

#물고기크기는 1~6, 9는 아기상어 위치
grid = [[*map(int,input().split())] for _ in range(n)]
fishes = dict()#물고기 정보 받아오기
for r in range(n):
    for c in range(n):
        if grid[r][c] == 9: shark=[r,c,2,0,0,0];grid[r][c]=0 #좌표1,좌표2, 크기, 먹은수, 시간, step
        elif grid[r][c]: fishes[(r,c)]=grid[r][c]

to = [[-1,0],[0,-1],[0,1],[1,0]]#상 좌 우 하
visited = [[0 for _ in range(n)] for _ in range(n)]
visited[shark[0]][shark[1]] = 1
q = deque([shark])
time = 0
cy,cx = shark[:2]
# grid[cy][cx] = 0
while q:
    try:
        y,x,s,e,t,step = q.popleft()
        if 0 < grid[y][x] < s:  # 0보단 크고 크기보다 작으면 먹을 수 있다.
            # print(f'ny = {ny} , nx = {nx}, value = {grid[ny][nx]} and size = {s}')
            grid[y][x] = 0
            visited = [[0 for _ in range(n)] for _ in range(n)]
            visited[y][x] = 1
            cy, cx = y, x
            time = t
            if e + 1 == s:  # 크기 커짐
                q = deque([[y, x, s + 1, 0, t , 0]])
            else:
                q = deque([[y, x, s, e + 1, t , 0]])
            raise Exception
        elif grid[y][x] == s or grid[y][x] == 0:
            for dy,dx in to:
                ny = y+dy; nx = x+dx
                if 0<=ny<n and 0<=nx<n and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    q.append([ny,nx,s,e,t+1,step+1])
                    q=deque(sorted(q,key = lambda x:(x[4],x[0],x[1])))

    except:
        continue
print(time)



"""
그냥 갖다 큐의 내용물을 정렬해 버리는데 두려움을 가지지 마라
heapq로는 key값을 하나밖에 쓰지 못하니 제한적.
-- 라고 생각했는데 숏코딩 한사람 보니 heapq에 [시간,행,열] 넣으면 순서대로 비교를 한다 []리스트 자체를 key 로 쓴다.
이외에 정렬을 간편하게 하면서 dfs를 할 방법이 없음 계속 edge case 발생.
일일히 다 정의하는게 훨~씬 어려움
"""

