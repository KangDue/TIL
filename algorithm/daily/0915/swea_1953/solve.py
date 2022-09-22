import sys
sys.stdin = open('input.txt')
"""
탈주범 검거
탈주범이 지하터널에 은신중
<터널타입>
0: 터널없음.
1: 상하좌우
p2: 상하
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
# po = {1:to, p2:to[:p2], 3:to[p2:], 4:[to[0],to[-1]], 5:[to[1],to[-1]], 6:[to[1],to[p2]], 7:[to[0],to[p2]]} #0,1 은 따질 것 없음
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
# from collections import deque
# to = [[-1,0], [1,0], [0,-1], [0,1]] #상하좌우
# po = {1:to, p2:to[:p2], 3:to[p2:], 4:[to[0],to[-1]], 5:[to[1],to[-1]], 6:[to[1],to[p2]], 7:[to[0],to[p2]]}
# for t in range(int(input())):
#     N,M,R,C,L=map(int,input().split())
#     grid = [[*map(int,input().split())] for _ in range(N)]
#     q = deque([[R,C,L]])
#     visited = [[0 for _ in range(M)] for _ in range(N)]
#     visited[R][C] = 1
#     while q:
#         y,x,l = q.popleft()
#         if l == 1: break
#         for dy,dx in po[grid[y][x]]:
#             ny = y+dy; nx = x + dx
#             if 0<=ny<N and 0<=nx<M and not visited[ny][nx] and grid[ny][nx]:
#                 for ddy,ddx in po[grid[ny][nx]]:
#                     if dy + ddy == 0 and dx + ddx == 0:
#                         q.append([ny,nx,l-1])
#                         visited[ny][nx] = 1
#     print(f'#{t+1} {sum(sum(visited,[]))}')

connect = {
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0],
}


def around(start, visited, queue):
    global count
    # 상하좌우 0 1 p2 3
    dx = [-1, 1, 0, 0]
    dy = [ 0, 0,-1, 1]
    a = start[0]
    b = start[1]
    if mat[a][b] != 0:
        pipe = mat[a][b]
        for i in range(4):
            if i == 0:
                if connect[pipe][i] == 1:
                    ni = a + dx[i]
                    nj = b + dy[i]

                    if 0 <= ni < N and 0 <= nj < M and mat[ni][nj]!= 0 and connect[mat[ni][nj]][1] == 1 and visited[ni][nj] == 0 :
                        visited[ni][nj] = visited[a][b] + 1
                        count += 1
                        queue.append((ni, nj))
            elif i == 1:
                if connect[pipe][i] == 1:
                    ni = a + dx[i]
                    nj = b + dy[i]

                    if 0 <= ni < N and 0 <= nj < M and mat[ni][nj]!= 0 and connect[mat[ni][nj]][0] == 1 and visited[ni][nj] == 0 :
                        visited[ni][nj] = visited[a][b] + 1
                        count += 1
                        queue.append((ni, nj))
            elif i == 2:
                if connect[pipe][i] == 1:
                    ni = a + dx[i]
                    nj = b + dy[i]

                    if 0 <= ni < N and 0 <= nj < M and mat[ni][nj]!= 0 and connect[mat[ni][nj]][3] == 1 and visited[ni][nj] == 0 :
                        visited[ni][nj] = visited[a][b] + 1
                        count += 1
                        queue.append((ni, nj))

            elif i == 3:
                if connect[pipe][i] == 1:
                    ni = a + dx[i]
                    nj = b + dy[i]

                    if 0 <= ni < N and 0 <= nj < M and mat[ni][nj]!= 0 and connect[mat[ni][nj]][2] == 1 and visited[ni][nj] == 0 :
                        visited[ni][nj] = visited[a][b] + 1
                        count += 1
                        queue.append((ni, nj))



def search():
    visited = [[0] * (N+1) for _ in range(M+1)]
    queue = [(R, C)]
    visited[R][C] = 1

    while queue:
        start = queue.pop(0)
        if visited[start[0]][start[1]] == L:
            return count
        around(start, visited, queue)


T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    # pprint(mat)
    count = 1
    search()
    print(f'#{tc} {count}')