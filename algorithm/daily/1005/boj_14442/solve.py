"""
벽부수고 이동하기 2
NxM grid
1은 벽이다.
최단경로를 찾자!
(시작,끝칸 포함)
이거도 복습하자!
"""
from collections import deque
o = open('input.txt')
R,C,K = map(int,next(o).split())
grid = [[*map(int,next(o).rstrip())] for _ in range(R)]
visited = [[[0,0] for _ in range(C)] for _ in range(R)]
to = [[1,0],[-1,0],[0,1],[0,-1]]
q = deque([[0,0]])
visited[0][0][0]= 1
while q:
    y,x = q.popleft()
    if (y,x) == (R-1,C-1):
        break
    for dy,dx in to:
        ny = y+dy; nx = x+dx
        if 0<=ny<R and 0<=nx<C:
            # 방문한 적이 없거나 있더라도 같은 벽을 깨더라도 덜 깨고 도달 가능
            if grid[ny][nx] and visited[y][x][1] < K and (not visited[ny][nx][0] or visited[ny][nx][1] > visited[y][x][1]+1):
                visited[ny][nx]=[visited[y][x][0],visited[y][x][1]+1]
                q.append([ny,nx])
            # 방문한 적이 없거나 있더라도 같은 벽을 깨더라도 덜 깨고 도달 가능
            elif not grid[ny][nx] and (not visited[ny][nx][0] or visited[ny][nx][1] > visited[y][x][1]):
                visited[ny][nx] = [visited[y][x][0]+1, visited[y][x][1]]
                q.append([ny, nx])
# print(*visited,sep='\n')
if visited[R-1][C-1][0]:
    print(sum(visited[R-1][C-1]))
else:
    print(-1)
"""
1. 벽을 만난다. -> 벽을 깬다.
2. 벽을 안만난다. -> 그냥 이동한다.
3. 같은곳으로 오긴 했는데 더 적은 벽을 깨고 왔다 = 갱신해준다.
"""