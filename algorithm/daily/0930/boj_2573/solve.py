import sys
sys.stdin = open('input.txt')
"""
빙산은 grid에 높이가 표시된다.
나머지는 0(바다)
바다에 많이 접한 부분이 더 빨리 녹음.(주변 0 개수만큼 녹음, 시간당)
빙산이 최초로 2덩이로 분리되는 시간.
다녹을때까지 분리가 안되면 0 출력

이 문제도 2차원말고 1차원으로 flatten후 풀면 더 빠를듯.
python3는 시간초과뜨고(70%쯤)
pypy는 868ms 

시간 1등 급 300ms 대
논리는 비슷함.
그리고 이 사람은 DFS임.
"""
def melt(y,x):
    for dy, dx in to:
        ny = y + dy; nx = x + dx
        if 0 <= ny < n and 0 <= nx < m and not grid[ny][nx]:
            temp[y][x] -= 1
    return None
from collections import deque
to = [[1,0],[-1,0],[0,1],[0,-1]]
n,m = map(int,input().split())
grid = [[*map(int,input().split())] for _ in range(n)]
tot = 0 # 총 개수
ice = dict()
for i in range(n):
    for j in range(m):
        if grid[i][j]:
            ice[(i,j)] = grid[i][j]
            tot += 1
t=0
while tot:
    t += 1
    temp = [[0] * m for _ in range(n)]
    for r,c in ice:
        melt(r,c)
    melted = []
    for r,c in ice:
        cal = grid[r][c] + temp[r][c]
        if cal<=0:
            grid[r][c] = 0
            tot -= 1
            melted.append((r,c))
        else:
            grid[r][c] = cal
            sy,sx = r,c
    for i in melted:
        ice.pop(i)
    # 그룹 확인.
    visited = [[0]*m for _ in range(n)]
    q = deque([[sy,sx]])
    visited[sy][sx] = 1
    count = 0
    while q:
        y,x = q.popleft()
        count += 1
        for dy,dx in to:
            ny = y + dy ; nx = x + dx
            if 0<=ny<n and 0<=nx<m and grid[ny][nx]:
                if not visited[ny][nx]:
                    visited[ny][nx] = 1
                    q.append([ny,nx])
    # print(*grid,sep ='\n')
    if tot and tot != count:
        print(t)
        break
else:
    print(0)
