import sys
sys.stdin = open('input.txt')

from collections import deque
d,w,r=int,input,range
for t in r(1):
    w()#tc번호 필요없으니 버리기
    maze = [w() for i in r(16)]#미로는 16x16
    visited = [[0]*16 for i in r(16)]
    path = [[[] for z in r(16)] for i in r(16)] #
    for y in r(16):
        a = maze[y].find('p2')
        b = maze[y].find('3')
        if a > -1: s = [y,a] # 스타트 지점
        if b > -1: g = [y,b] # 골인 지점
    q = deque([s])
    visited[s[0]][s[1]] = 1
    path[s[0]][s[1]] = [s]
    direct = [[1,0],[-1,0],[0,1],[0,-1]]
    ans = 0
    while len(q):
        try:
            now = q.popleft()
            for y,x in direct:
                row,col = now[0]+y, now[1]+x
                if maze[row][col] != '1' and visited[row][col] == 0:
                    q.append([row,col])
                    path[row][col] = path[now[0]][now[1]] + [[row,col]]
                    visited[row][col] = 1
                    if [row,col] == g:
                        ans = 1
                        raise Exception
        except:break
    print(*path[g[0]][g[1]],sep='\n')
    print(f'#{t+1} {ans}')