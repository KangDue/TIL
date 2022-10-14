"""
불켜기
NxN칸 헛간에서 1,1~N,N까지
chleogks qnfdmf qkfrglwk
1,1 (유일하게 켜진곳)에서 출발
각 방에서는 다른 방의 불을 켤  수 있다.
한 방에 여러 스위치가 있을 수 있다.
하나의 방의 불 스위치도 여러개일 수 있다.
x y a b 는 x,y에서 a,b 불을 켤 수 있다는 뜻.
불 킬 수 있는 방의 최대 개수를 구하시오.

#1차시도 1번만 맞음.
"""
import sys,time
sys.stdin = open('input.txt')

# M 스위치 정보
from collections import defaultdict
to = [[1,0],[0,1],[-1,0],[0,-1]]
N,M = map(int,input().split())
grid = [[0]*(N+1) for _ in range(N+1)]
grid[1][1] = 1
info = defaultdict(list)
for _ in range(M):
    x,y,a,b = map(int,input().split())
    info[(y,x)].append((b,a))
# print(info)

turnon = [[0]*(N+1) for _ in range(N+1)]

ans = 1
step = 0
visited = [[0]*(N+1) for _ in range(N+1)]
while 1:
    step += 1
    q = [(1,1)]
    visited[1][1] = step
    count = 0
    while q:
        new = []
        for point in q:
            if not turnon[point[0]][point[1]]:
                turnon[point[0]][point[1]] = 1
                for r,c in info[point]:
                    if not grid[r][c]:
                        grid[r][c] = 1 # 불키는 걸 1로 하자
                        count += 1 #새로 불키는 횟수
            for dy,dx in to:
                ny, nx = point[0]+dy, point[1]+dx
                if 1<= ny <=N and 1<= nx <= N and grid[ny][nx] and visited[ny][nx] != step:
                    new.append((ny,nx))
                    visited[ny][nx] = step
        q = new
    ans += count
    if not count:
        break
print(ans)

def dist(a, b): # 방향 전환 굳 아이디어
    yield a+1,b;yield a-1,b;yield a,b+1;yield a,b-1