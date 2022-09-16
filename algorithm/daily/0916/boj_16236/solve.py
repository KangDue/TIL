import sys
sys.stdin = open('input.txt')
"""
NxN공간 물고기 M마리 , 아기 상어 1마리
한칸에 최대 물고기 1마리
상어 물고기 모두 각자의 크기가 있고
상어는 자기보다 큰 물고기 못지나침(못먹음)
크기가 같으면 지나는 가지만 못먹음
- 더 이상 먹을 고기가 없다 = mom call
- 남은 고기 1마리면 바로 ㄱㄱ(그냥 1step씩)
- 1마리보다 가까우면 최단거리로
- 거리가 가까운게 여러마리면 가장 위, 가장 왼쪽부터
- 이동은 1초, 먹는데 시간 소모 x 먹으면 빈칸됨.
- 자기 크기랑 같은 수의 물고기를 먹으면 크기 1 증가
- 몇초동안 엄마를 안부르고 고기를 먹을수 있나 ?

-처음크기 = 2, 상하좌우로 1칸씩 이동가능.
-단순 bfs라기보단 물고기 좌표를 알아야하니 조합같음 - 못지나가는 경로 판단이 안됨. - bfs 가자
"""
from math import dist
from collections import deque,defaultdict
def check(arr):
    diff = set(fishes).difference(set(h))
    print(h)
    for i in diff:
        if fishes[i]<s:
            return 1
    else: return 0
n = int(input())
#물고기크기는 1~6, 9는 아기상어 위치
grid = [[*map(int,input().split())] for _ in range(n)]
fishes = dict()
for r in range(n):
    for c in range(n):
        if grid[r][c] == 9: shark=[r,c,2,0,0,[]]
        elif grid[r][c]: fishes[(r,c)]=grid[r][c]
to = [[-1,0],[0,-1],[1,0],[0,1]]
visited = [[0 for _ in range(n)] for _ in range(n)]
q = deque([shark])
visited[shark[0]][shark[1]] = 1
mv = 0
while q:
    y,x,s,t,e,h = q.popleft()
    print(h)
    if not check(h): continue
    mv = max(mv,t)
    for dy,dx in to:
        ny = y+dy; nx = x+dx
        if 0<=ny<n and 0<=nx<n:
            if 0< grid[ny][nx] <s:#0보단 크고 크기보다 작으면 먹을 수 있다.
                grid[ny][nx] = 0
                if e+1 == s: # 크기 커짐
                    q.append([ny,nx,s+1,t+1,0,h+[(r,c)]])
                else:
                    q.append([ny, nx, s, t + 1, e+1,h+[(r,c)]])
            else:
                q.append([ny,nx,s,t+1,e,h])
print(t)