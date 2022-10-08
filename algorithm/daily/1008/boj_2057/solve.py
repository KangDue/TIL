"""
마법사 상어와 토네이도
NxN 격자에서 마법사 상어가 토네이도 연습
가운데 칸부터 이동이 시작된다., (1,1) (가장 왼쪽, 위) 에서 소멸
토네이도거 y에서 x로 이동시 비율이 적혀 있는 칸의 비율을 따라 흩날린다.
소수점 아래는 버린다.
각 grid에 칸에는 모래 양이 주어짐.
grid 밖으로 나갈 수도 있는데 밖으로 나가버린 모레의 양을 구하시오.
날려버리면 칸에는 55프로가 항상 남음.
"""
import sys
sys.stdin = open('input.txt')
from collections import deque
from math import trunc
to = [[0,-1],[1,0],[0,1],[-1,0]]#좌 하 우 상 (0,1,2,3)
n = int(input())
grid = [[0]*(n+2)] + [[0]+[*map(int,input().split())]+[0] for _ in range(n)] + [[0]*(n+2)]
visited = [[0]*(n+2) for _ in range(n+2)]
# print(*grid,sep='\n')

blown = 0
def blow(r,c,d):#좌표, 방향
    global blown
    #좌측 기준 생성
    sand = grid[r][c]
    y, x = to[d]
    temp2 = [0.05, 0.1, 0.1, 0.02, 0.07, 0.07, 0.02, 0.01, 0.01]
    if d == 0 or d == 2: #d랑, 곱하는 값을 똑바로 집중해서 설정하자 ^^ d가아니라 x,y를 해야지!
        temp1= [[r,c + 2*x],[r - 1,c + 1*x], [r + 1,c + 1*x],
                [r + 2,c], [r + 1,c], [r - 1,c], [r - 2,c],
                [r - 1,c - 1*x], [r + 1,c - 1*x]]
    else:
        temp1= [[r + 2*y,c], [r + 1*y,c - 1], [r + 1*y,c + 1],
                [r,c + 2], [r,c + 1], [r,c - 1], [r,c - 2],
                [r - 1 * y,c - 1], [r - 1*y,c + 1]]
    rem = grid[r][c]
    for i in range(9):
        nr,nc = temp1[i]
        if 1<=nr<=n and 1<=nc<=n:
            v = trunc(temp2[i]*sand)
            grid[nr][nc] += v
            rem -= v
        else:
            v = trunc(temp2[i]*sand)
            blown += v
            rem -= v
    nr,nc = r+to[d][0], c+to[d][1]
    if 1<=nr<=n and 1<=nc<=n:
        grid[nr][nc] += rem
    else:
        blown += rem
    grid[r][c]=0

q = deque([[n//2+1,n//2+1]])
visited[n//2+1][n//2+1] = 1
d = 0
while q:
    y,x = q.popleft()
    ny = y+to[d][0]
    nx = x+to[d][1]
    if 1<=ny<=n and 1<=nx<=n and not visited[ny][nx]: #간적 없는 칸으로만 1칸씩!
        visited[ny][nx] = 1
        q.append([ny,nx])
        ex = d
        blow(ny, nx, d)
        d = (d+1)%4
    else:
        ny = y + to[ex][0]
        nx = x + to[ex][1]
        if 1 <= ny <= n and 1 <= nx <= n and not visited[ny][nx]:  # 간적 없는 칸으로만 1칸씩!
            visited[ny][nx] = 1
            q.append([ny, nx])
            blow(ny, nx, ex)
print(blown)

print(*visited,sep='\n')
print()
print(*grid,sep='\n')