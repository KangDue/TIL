import sys
sys.stdin = open('input.txt')

T = int(input())

def bfs_miro(a, b, N, mat):
    visited = [[0] * N for _ in range(N)]
    queue = []
    queue.append([a, b, -1])
    visited[a][b] = 1
    while queue:
        a, b, h = queue.pop(0)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni = a + dx
            nj = b + dy
            if 0 <= ni < N and 0 <= nj < N and mat[ni][nj] != 1 and visited[ni][nj] == 0:
                c = ni
                d = nj
                queue.append([c, d, h+1])
                visited[c][d] = 1
            if 0 <= ni < N and 0 <= nj < N and mat[ni][nj] == 2:
                return h+1
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 3:
                a = i
                b = j
                break
    result = bfs_miro(a, b, N, mat)
    if not result:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {result}')


