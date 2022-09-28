import sys
sys.stdin = open('input.txt')
"""
연구소(n x m)
바이러스가 퍼지지 않게 벽 3개를 반드시 세우고
안전영역의 넓이를 구하라.
nxm 그리드에서 벽 3개를 어떻게 잘 세워야 할까 고민 조금 해보았지만
brute force밖에 방법이 없음.
그나마 여기서 조건을 달아 벽 주변에 이어 붙여야한다거나 하는걸 추가 할순 있지만
ex) 벽 대각선 이나 상하좌우 방향에만 이어 붙일 수 있다.(연구소 밖도 벽처리 후)
그럴거면 컴퓨터 왜씀? ㅋ
n x m 어차피 3x3~8x8 범위
64개 중에서도 3개 뽑는 경우의수는 40000개 정도 밖에 안됨.
1. 일단은 brue force (no limit)으로 갈겨보자
"""
from collections import deque
from itertools import combinations as cb
n,m = map(int,input().split())
grid =[[1]*(m+2)] + [[1]+[*map(int,input().split())]+[1] for _ in range(n)] + [[1]*(m+2)]
to = [[1,0],[-1,0],[0,1],[0,-1]]
empty = []
virus = []
tot = 0 # 초기 빈 공간 크기.
for i in range(1,n+2):
    for j in range(1,m+2):
        if grid[i][j] == 2:
            virus.append([i,j])
        elif not grid[i][j]:
            empty.append([i,j])
            tot += 1
def area():
    q = deque(virus)
    ngrid = [[grid[i][j] for j in range(m+2)] for i in range(n+2)]
    temp = 0 # 감염 영역의 넓이
    while q:
        y,x = q.popleft()
        for dy,dx in to:
            ny = y+dy; nx = x+dx
            if not ngrid[ny][nx]: #빈 곳만 갈 수 있다.
                q.append([ny,nx])
                ngrid[ny][nx]=2 #어디서 자꾸 오류가 쳐 나나 했는데 그리드가 복구가 안된거네 ...
                temp += 1
    return tot-temp # 안전 영역의 수

maxv = 0
for new_wall in cb(empty,3): # 브루트 포스
    for y,x in new_wall: # 벽 세우기
        grid[y][x] = 1
    maxv = max(maxv,area())
    for y,x in new_wall: # 벽 무너뜨리기
        grid[y][x] = 0
print(maxv-3) #3개의 벽 개수 차감