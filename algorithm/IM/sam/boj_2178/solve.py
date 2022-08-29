import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
미로
0은 벽, 1은 길
1,1출발 n,m까지 가는데 필요한 칸수 ( 시작점 포함)
"""
if __name__ == "__main__":
    import sys
    r, sr = range, sys.stdin.readline
    from collections import deque,defaultdict
    row,col = map(int,sr().split())
    maze = [sr() for i in range(row)]
    visited = [[0 for i in range(col)] for j in range(row)]
    start = [0,0]
    goal = [row-1,col-1]

    q = deque([[start[0],start[1],1]])
    visited[start[0]][start[1]] = 1
    to = [[1,0],[-1,0],[0,1],[0,-1]]
    while q:
        y,x,step = q.popleft()
        if [y,x]==goal:
            print(step)
            break
        for dy,dx in to:
            ny = y + dy; nx = x + dx
            if 0 <= ny < row and 0 <= nx < col: # 유효범위고 길일떄
                if visited[ny][nx] == 0 and maze[ny][nx]=='1': #간적이 없다면
                    visited[ny][nx] = 1
                    q.append([ny,nx,step+1])
