"""
말이 되고픈 원숭이
원숭이가 체스말 처럼 k번만 움직일 수 있다.
이후에는 인접칸으로만 움직임.
말의 움직임으로는 장애물도 뛰어 넘음.
원숭이가 움직일때 말처럼 움직이든, 그냥 인접한칸 가든 이동 한번당 스텝 하나로 침.
격자판이 주어질 때 원숭이가 최소한의 동작으로 시작지점에서 도착지점까지 갈 수 있는 방법의
개수가 아니라 도착점까지 최소 step 수는 ?, 도달 불가시 -1 출력.
장애물 1, 평지 0
RxC의 grid가 주어짐.
#시간 초과 뜨네?

방법을 바꿔보자
31%까지는 가네? ㅎㅎ;
25% 아오
이 dog 같은 문제 나중에 또해보자!
"""

from collections import deque
o = open('input.txt')
K = int(next(o))
C,R = map(int,next(o).split()) #열 개수, 행 개수 ,순서 주의
grid = [[*map(int,next(o).split())] for _ in range(R)]
visited = [[[0,0] for _ in range(C)] for _ in range(R)] # [0,0]에서 0은 원숭이 방문, 1은 말 방문
to = [[1,0],[-1,0],[0,1],[0,-1]]
horse = [[-2,-1],[-2,1],[-1,-2],[1,-2],[2,-1],[2,1],[-1,2],[1,2]]#말과 원숭이 움직임
q = deque([[0,0]])
visited[0][0]=[1,0]
while q: #말 move로 방문한 곳은 , 원숭이 move로도 갈 수 있게 처리해야함.
    try:
        y,x = q.popleft()
        for dy, dx in to:
            ny = y + dy;
            nx = x + dx
            #원숭이 스텝으로 방문한 적이 없거나, 한 적이 있어도 말스텝을 덜 썻다면 ㄱ
            if 0 <= ny < R and 0 <= nx < C and not grid[ny][nx] and (not visited[ny][nx][0] or visited[ny][nx][1] > visited[y][x][1]):
                q.append([ny, nx])
                visited[ny][nx][0] = visited[y][x][0]+1
                visited[ny][nx][1] = visited[y][x][1]
                if (ny, nx) == (R - 1, C - 1):
                    print(sum(visited[R - 1][C - 1]) - 1)
                    raise Exception
        if visited[y][x][1] < K: #말은 원숭이가 방문한 곳에 갈 필요가 없다.
            for dy,dx in horse:
                ny = y+dy; nx = x + dx
                #원숭이 스텝으로 방문한 적이 없거나, 한 적이 있어도 말스텝을 덜 썻다면 ㄱ
                if 0 <= ny < R and 0 <= nx < C and not grid[ny][nx] and (not visited[ny][nx][0] or visited[ny][nx][1] > visited[y][x][1] + 1):
                    q.append([ny,nx])
                    visited[ny][nx][1] = visited[y][x][1]+1
                    visited[ny][nx][0] = visited[y][x][0]
                    if (ny,nx)==(R-1,C-1):
                        print(sum(visited[R - 1][C - 1]) - 1)
                        raise Exception
    except:
        break
else:
    if visited[R-1][C-1][0] or visited[R-1][C-1][1]:
        print(sum(visited[R - 1][C - 1]) - 1)
    else:
        print(-1)
# print(*visited,sep='\n')
