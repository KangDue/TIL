import sys
sys.stdin = open('input.txt')
"""
보급로
가장짧은 경로에 대한 총 복구시간 구하기\
"""
to = [[1,0],[-1,0],[0,1],[0,-1]]
import heapq
for t in range(int(input())):
    n = int(input())
    grid = [[*map(int,input())] for _ in range(n)]
    visited = [[0]*n for i in range(n)]
    q = [[0,0,0]]
    visited[0][0]=1
    while q:
        d,y,x = heapq.heappop(q)
        if (y,x)==(n-1,n-1):
            break
        for dy,dx in to:
            ny=y+dy;nx=x+dx
            if 0<=ny<n and 0<=nx<n:
                if not visited[ny][nx]:
                    visited[ny][nx] = 1
                    heapq.heappush(q,[d+grid[ny][nx],ny,nx])
    print(f'#{t+1 } {d}')



