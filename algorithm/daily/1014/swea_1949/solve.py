"""
등산로 조성
NxN 등산로 높이가 각 칸에 주어짐
가장 높은 봉우리에서 시작.
반드시 높은곳에서 낮은곳으로 연결
딱 한 곳을 정해서 최대 K 만큼 높이 낮출 수 있음.
가장 긴 등산로를 찾고 그 길이 출력
#1. 일단 n**3 브루트 포스 갈기기

#top 이 1개면 1개를 깎아서 다른 top 을 쓸 수도 있다.
"""
import sys
sys.stdin = open('input.txt')

to = [[1,0],[-1,0],[0,1],[0,-1]]
for t in range(int(input())):
    N,K = map(int,input().split())
    grid = [[*map(int,input().split())] for _ in range(N)]
    visited = [[0 for i in range(N)] for j in range(N)]
    pick = [[] for i in range(21)] #높이 20 이하 정수
    for i in range(N):
        for j in range(N):
            pick[grid[i][j]].append((i,j))
    top = 0
    for i in range(20,-1,-1):
        if pick[i]:
            top = i
            break
    maxv = 0
    def dfs(r,c,length=1,flag=1):
        global K,N,visited,maxv
        maxv = max(maxv, length)
        for dy,dx in to:
            ny = r + dy
            nx = c + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:# 유효범위, 사방, 낮은 곳으로.
                if grid[r][c] > grid[ny][nx]:
                    visited[ny][nx] = 1
                    dfs(ny, nx, length + 1, flag)
                    visited[ny][nx] = 0
                else:
                    for k in range(1,K+1):
                        if flag and grid[r][c] == grid[ny][nx] - k + 1:
                            grid[ny][nx] -= k  # 깎아보기
                            visited[ny][nx] = 1
                            dfs(ny, nx, length + 1, 0) # 깎아 버렸음.
                            visited[ny][nx] = 0
                            grid[ny][nx] += k
    for r,c in pick[top]:
        for k in range(K+1):
            visited[r][c] = 1
            grid[r][c] -= k
            dfs(r,c,1,not k)
            grid[r][c] += k
            visited[r][c] = 0

    print(f'#{t+1} {maxv}')









