import sys
sys.stdin = open('input.txt')
"""
최소비용
"""
import heapq
to = [[1,0],[-1,0],[0,1],[0,-1]]
INF = int(1e9)
for t in range(int(input())):
    n = int(input())
    grid = [[*map(int,input().split())] for _ in range(n)]
    q = [[0,0,0]] # tot,y,x
    dist = [[INF]*n for _ in range(n)]
    while q:
        tot,y,x = heapq.heappop(q)
        if tot > dist[y][x]:
            continue
        for dy,dx in to:
            ny = y+dy; nx = x + dx
            if 0<=ny<n and 0<=nx<n:
                #높이차 절대값이 아니라 높은곳으로 갈때만 추가비용
                extra = grid[ny][nx]-grid[y][x] if grid[ny][nx] > grid[y][x] else 0
                cost = tot + extra + 1
                if cost < dist[ny][nx]:
                    dist[ny][nx] = cost
                    heapq.heappush(q,[cost,ny,nx])
    print(f'#{t+1} {dist[n-1][n-1]}')