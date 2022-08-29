import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
보통 메모리 초과는 종료조건 ...
탈옥!
죄수들이 겹치면 안된다는 조건은 딱히 없다.
"""
if __name__ == "__main__":
    import sys
    sr = sys.stdin.readline
    from collections import deque
    for t in range(int(sr())):
        R,C = map(int,sr().split())
        maze = [['.']+[*sr().strip()]+['.'] for i in range(R)]
        maze = [['.']*(C+2)]+maze+[['.']*(C+2)]
        p=[]
        for i in range(R+2):
            for j in range(C+2):
                if maze[i][j] == '$':
                    p.append([i,j])
        to = [[1,0],[0,1],[-1,0],[0,-1]]
        def bfs(y,x):#시작지점
            q = deque([[y,x]])
            visited = [[-1 for i in range(C+2)] for j in range(R+2)]
            visited[y][x] += 1
            while q:
                yy,xx = q.popleft()
                for dy,dx in to:
                    ny=yy+dy; nx = xx+dx
                    if 0<= ny < R+2 and 0<= nx < C+2:
                        if visited[ny][nx] == -1 and maze[ny][nx] == '#':
                            visited[ny][nx] = visited[yy][xx] + 1
                            q.append([ny,nx])
                        elif visited[ny][nx] == -1 and maze[ny][nx] in '.$':
                            visited[ny][nx] = visited[yy][xx]
                            q.appendleft([ny,nx])
            return visited
        p1=bfs(p[0][0],p[0][1])
        p2=bfs(p[1][0],p[1][1])
        out=bfs(0,0)
        ans = 10001
        for i in range(R+2):
            for j in range(C+2):
                if p1[i][j] != -1 and p2[i][j] != -1 and out[i][j] != -1:#길이라면
                    res = p1[i][j] + p2[i][j] + out[i][j]
                    if maze[i][j] == '#':
                        res -= 2
                    ans = min(ans,res)
        print(ans)

# from collections import deque
# t = int(input())
# dx = [-1, 0, 0, 1]
# dy = [0, -1, 1, 0]
#
#
# def bfs(m, i, j):
# 	r = len(m)
# 	a = len(m[0])
# 	d = [[-1] * a for _ in range(r)]
# 	q = deque()
# 	q.append((i, j))
# 	d[i][j] = 0
# 	while q:
# 		x, y = q.popleft()
# 		for k in range(4):
# 			nx, ny = x + dx[k], y + dy[k]
# 			if 0 <= nx < r and 0 <= ny < a and d[nx][ny] == -1 and m[nx][ny] != '*':
# 				if m[nx][ny] == '#':
# 					d[nx][ny] = d[x][y] + 1
# 					q.append((nx, ny))
# 				else:
# 					d[nx][ny] = d[x][y]
# 					q.appendleft((nx, ny))
# 	return d
#
#
# while t:
# 	h, w = map(int, input().split())
# 	m = ['.' + input() + '.' for _ in range(h)]
# 	h += 2
# 	w += 2
# 	m = ['.' * w] + m + ['.' * w]
# 	c = []
# 	ans = 10000
# 	d0 = bfs(m, 0, 0)
# 	for i in range(h):
# 		for j in range(w):
# 			if m[i][j] == '$':
# 				c.append((i, j))
# 	d1 = bfs(m, c[0][0], c[0][1])
# 	d2 = bfs(m, c[1][0], c[1][1])
# 	for i in range(h):
# 		for j in range(w):
# 			if d0[i][j] == -1 or d1[i][j] == -1 or d2[i][j] == -1:
# 				continue
# 			if m[i][j] == '*':
# 				continue
# 			cur = d0[i][j] + d1[i][j] + d2[i][j]
# 			if m[i][j] == '#':
# 				cur -= 2
# 			ans = min(ans, cur)
# 	print(ans)
# 	t -= 1
