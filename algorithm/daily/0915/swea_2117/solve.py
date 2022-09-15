import sys
sys.stdin = open('input.txt')
"""
방범서비스
KxK 정사각형에서 마름모 꼴로만 방법서비스를 제공
실제 운영지역은 마름모의 일부여도 가능하다.
운영비용은 K*K + (K-1)*(K-1)
서비스 받는 집들은 비용 M을 지불
회사는 손해 안보는선에서 최대한 많은집에 서비스 제공하려함
이떄 서비스를 받는 집의 수 출력
도시 정보에서 1은 집이있는 곳
"""
from collections import deque
from itertools import accumulate as ac
to = [[1,0],[-1,0],[0,1],[0,-1]]
def search(r,c): #좌표기준 마름모 확장하며 탐색;
    global N,M,grid
    visited = [[0 for _ in range(N)] for _ in range(N)]
    q = deque([[r,c,1]])#좌표와 k값
    visited[r][c] = 1
    sur = [0 for _ in range(2*N)]
    people = [0 for _ in range(2*N)]
    for K in range(1,len(sur)):
        sur[K] = -(K * K + (K - 1) * (K - 1)) #초기 운영비용, 집 수
    if grid[r][c] == '1':
        people[1] += 1
    while q:
        y,x,d = q.popleft()
        if d == 2*N: break
        for dy,dx in to:
            ny = y+dy; nx = x+dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                visited[ny][nx] = 1
                if grid[ny][nx] == '1': #중간에 멈추는건 안됨. 갑자기 집이 많아질수도 있음.
                    people[d+1] += 1
                q.append([ny,nx,d+1])
    idx = 0
    mv = 0
    re = []
    for i in ac(people):
        sur[idx] += M*i
        if sur[idx] > -1 :
            mv = i
            re.append([i,sur[idx]])
        idx += 1
    return mv
for t in range(int(input())):
    N,M = map(int,input().split())
    grid = [input().split() for _ in range(N)] #굳이 형변환 할 필요 없음.
    mv = 0
    for r in range(N):
        for c in range(N):
            mv=max(mv,search(r, c))
    print(f'#{t+1} {mv}')






