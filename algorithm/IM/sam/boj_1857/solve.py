import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
발레리노
체스의 나이트처럼 이동가능
최소한의 방석으로 김조교가 시작점에서 끝까지 갈 수 있게하고
그 방법이 몇가지인지 나타내기
돌맹이는 방석 x
3이 시작, 4가 도착점. (시작과 출발 정해져서 dijkstra 써도 될 것 같은디 ㅎㅎ;
하지만 bfs 정석으로 가자!

1. 도착점으로 가는 모든 경로를 구한다.
2. 도착점으로 가는 모든 경로와 도중에 방석이 있다면 카운트해준다.
3. 시작과 끝에도 방석이 있당.
4. 어떤 경로에 도달하기까지 step수와 방석수를 같이 기록하자!?
"""
if __name__ == "__main__":
    import sys
    sr = input
    from collections import deque
    R,C = map(int,sr().split())
    pan = [[*map(int,sr().split())] for i in range(R)]
    for i in range(R):
        for j in range(C):
            if pan[i][j] == 3:
                start = [i,j]
            if pan[i][j] == 4:
                end = [i,j]
    linked = [[[] for i in range(C)] for j in range(R)]#노드별 연결장소 담기
    def register(y,x,yy,xx):
        visited[yy][xx] = 1
        if pan[yy][xx] == 2:
            return
        if pan[yy][xx] != 1 and not(yy==y and xx==x):
            linked[y][x].append([yy, xx])
            return
        for dy,dx in to:
            ny =yy+dy; nx = xx+dx
            if 0<= ny < R and 0<= nx < C and visited[ny][nx]==0:
                register(y,x,ny,nx)
            else:continue

    q = deque([[start[0],start[1]]]) #시작 방석은 세지않고 마지막 방석은 나중에 빼주자
    to = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, -1], [2, 1], [-1, -2], [1, -2]]
    for i in range(R):
        for j in range(C):
            visited = [[0 for _ in range(C)] for _ in range(R)]
            register(i,j,i,j)
    seat = [[0 for i in range(C)] for j in range(R)]#방석수/방문여부
    possible = [[0 for i in range(C)] for j in range(R)]#경우의수
    seat[start[0]][start[1]] = 1
    possible[start[0]][start[1]] = 1
    while q:
        y,x = q.popleft()
        for i in linked[y][x]:
            ny=i[0];nx=i[1]
            if seat[ny][nx] == 0:
                seat[ny][nx] = seat[y][x] + 1
                possible[ny][nx] = possible[y][x]
                q.append([ny, nx])
            elif seat[ny][nx] == seat[y][x] + 1:
                possible[ny][nx] += possible[y][x]
    if seat[end[0]][end[1]]:
        print(seat[end[0]][end[1]]-2)
        print(possible[end[0]][end[1]])
    else: print(-1)