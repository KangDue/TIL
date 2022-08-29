import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
벽뚫고가기
0은 길 1은 벽
1,1에서 n,m 까지 이동
최단 거리 또는 불가능은 -1
벽을 최대 한개까지 부숴도 된다.
"""
if __name__ == "__main__":
    import sys
    r, sr = range, sys.stdin.readline
    from collections import deque,defaultdict
    row,col = map(int,sr().split())
    maze = [list(map(int,sr().strip())) for i in range(row)]
    visited = [[ [0,0] for i in range(col)] for j in range(row)] #visited를 통쨰로 따로 만드는것보다 [0,0]으로 분리해서 관리하는것이 메모리를 아낀다.
    start = [ 0, 0 ]
    goal = [row-1,col-1]
    q = deque([[start[0],start[1],1,0]]) #y,x,step,crash
    to = [[1,0],[-1,0],[0,1],[0,-1]]
    visited[0][0][0] = 1
    while q:
        y,x,step,crash = q.popleft()
        #같은 길이어도 벽을뚫고가거나 안뚫고 갈수도 있으니 중복체크 해야함.
        if [y,x] == goal:
            print(step)
            break
        for dy,dx in to:
            ny = y+dy; nx = x+dx
            if 0<= ny < row and 0<= nx < col:
                if visited[ny][nx][0] == 0 and crash == 0: #벽 깬적이 없을때
                    if maze[ny][nx] and crash == 0:#다음이 벽이고 깬적이 없다면 crash 1 추가
                        q.append([ny,nx,step+1,1])
                        visited[ny][nx][1] = 1
                    elif maze[ny][nx] == 0: #다음이 길이면
                        q.append([ny,nx,step+1,0])
                        visited[ny][nx][0] = 1
                elif visited[ny][nx][1] == 0 and crash == 1: #벽한번 깬 놈들은 여기서 관리
                    if maze[ny][nx] == 0: #길일때만 본다.
                        q.append([ny, nx, step + 1, 1])
                        visited[ny][nx][1] = 1

    else:
        print(-1)