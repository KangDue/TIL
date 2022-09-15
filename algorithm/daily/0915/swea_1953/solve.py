import sys
sys.stdin = open('input.txt')
"""
탈주범 검거
탈주범이 지하터널에 은신중
<터널타입>
0: 터널없음.
1: 상하좌우
2: 상하
3: 좌우
4: 위와 오른쪽 연결
5: 아래랑 오른쪽 연결
6: 아래랑 왼쪽 연결
7: 위랑 왼쪽 연결
좌표는 2차원 행렬 INDEX와 같다.
탈주범이 특정시간뒤에 도착할 수 있는 장소의 개수
"""
# from collections import deque
# to = [[-1,0], [1,0], [0,-1], [0,1]] #상하좌우
# po = {1:to, 2:to[:2], 3:to[2:], 4:[to[0],to[-1]], 5:[to[1],to[-1]], 6:[to[1],to[2]], 7:[to[0],to[2]]} #0,1 은 따질 것 없음
# for t in range(int(input())):
#     N,M,R,C,L=map(int,input().split()) #지도 높이 넓이, 탈주범 맨홀뚜껑 좌표, 탈주 후 지난 시간
#     grid = [[*map(int,input().split())] for _ in range(N)]
#     q = deque([[R,C,L]])
#     visited = [[0 for _ in range(M)] for _ in range(N)]
#     visited[R][C] = 1
#     while q:
#         y,x,l = q.popleft()
#         if l == 1: break
#         for dy,dx in po[grid[y][x]]:#갈수 있는 방향보기
#             ny = y+dy; nx = x + dx
#             if 0<=ny<N and 0<=nx<M and not visited[ny][nx] and grid[ny][nx]: #조건을 ny//N<1 이렇게 하면 -로 가버림.
#                 for ddy,ddx in po[grid[ny][nx]]: #갈 곳과 연결 가능한지 확인
#                     if dy + ddy == 0 and dx + ddx == 0: # 두 이동의 합이 영이면 이동 가능
#                         q.append([ny,nx,l-1])
#                         visited[ny][nx] = 1
#     print(f'#{t+1} {sum(sum(visited,[]))}')

#길이를 줄여보자
from collections import deque
to = [[-1,0], [1,0], [0,-1], [0,1]] #상하좌우
po = {1:to, 2:to[:2], 3:to[2:], 4:[to[0],to[-1]], 5:[to[1],to[-1]], 6:[to[1],to[2]], 7:[to[0],to[2]]}
for t in range(int(input())):
    N,M,R,C,L=map(int,input().split())
    grid = [[*map(int,input().split())] for _ in range(N)]
    q = deque([[R,C,L]])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[R][C] = 1
    while q:
        y,x,l = q.popleft()
        if l == 1: break
        for dy,dx in po[grid[y][x]]:
            ny = y+dy; nx = x + dx
            if 0<=ny<N and 0<=nx<M and not visited[ny][nx] and grid[ny][nx]:
                for ddy,ddx in po[grid[ny][nx]]:
                    if dy + ddy == 0 and dx + ddx == 0:
                        q.append([ny,nx,l-1])
                        visited[ny][nx] = 1
    print(f'#{t+1} {sum(sum(visited,[]))}')