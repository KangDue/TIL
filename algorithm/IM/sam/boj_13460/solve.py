import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
구슬탈출!
빨간 구슬을 최소 10회 안에 탈출 시켜라!
파란 구슬이 먼저나오면 fail
1.최소? = bfs로가자
2.모든 경우를 다봐야하니까 bfs` 재귀로 해보자
--- 1시간 컷 실패. ㅠ
"""
if __name__ == "__main__":
    import sys
    from collections import deque
    r=range
    sr = sys.stdin.readline
    n,m = map(int,sr().split())
    grid = [ input() for i in range(n)]
    for i in range(n):
        t1 = grid[i].find('R')
        t2 = grid[i].find('B')
        t3 = grid[i].find('O')
        if t1 > -1: red = [i,t1]
        if t2 > -1: blue = [i,t2]
        if t3 > -1: goal = [i,t3]
    visited = [[[[0 for _ in range(m)] for _ in range(n)] for i in range(m)] for j in range(n)]
    visited[red[0]][red[1]][blue[0]][blue[1]] = 1

    def incline(y,x,dy,dx):
        step = 0
        while grid[y+dy][x+dx] != '#' and grid[y][x] != 'O':
            x += dx; y += dy; step += 1
        return y,x,step
    q = deque([[red[0],red[1],blue[0],blue[1],0]]) #빨강,파랑 위치, 기울인 횟수
    to = [[1, 0], [-1, 0], [0, -1], [0, 1]]  # 방향
    def bfs():
        while q:
            ry,rx,by,bx,inc = q.popleft()
            if inc+1 > 10: break#10번 넘어가면 실패
            for dy,dx in to:
                nry,nrx,rc = incline(ry,rx,dy,dx)
                nby,nbx,bc = incline(by,bx,dy,dx)
                if grid[nby][nbx] == 'O': #빨강이 먼저오면 잘못된 case로 끝남.
                    continue #다른 방향으로 기울이기
                if grid[nry][nrx] == 'O': print(inc+1); return #아래 도달하지않고 끝나니까 1추가
                if (nry,nrx) == (nby,nbx): #구슬 겹치면 한놈 뒤로 빼기
                    if rc < bc: nby -= dy; nbx -= dx
                    else: nry -= dy; nrx -= dx
                if not visited[nry][nrx][nby][nbx]:
                    visited[nry][nrx][nby][nbx] = 1
                    q.append([nry,nrx,nby,nbx,inc+1])
        print(-1)
    bfs()





    # fr=fb=False
    # while redq and blueq: # 둘다 갈 곳이 없다면 끝
    #     rn = redq.popleft()
    #     bn = blueq.popleft()
    #     for dd in di:
    #         rc,rl = rn[0]+dd[0], rn[1]+dd[1]
    #         bc,bl = bn[0]+dd[0], bn[1]+dd[1]
    #         if 0 <= rc < n and 0 <= rl < m:
    #             if grid[rc][rl] != '#' and rvisited[rc][rl] == 0:#벽이 아니고 방문한적 없다면
    #                 while grid[rc][rl] != '#':
    #                     rvisited[rc][rl] = rvisited[rn[0]][rn[1]] + 1
    #                     rc += dd[0]
    #                     rl += dd[1]
    #                 redq.append([rc,rl])
    #         if 0 <= bc < n and 0 <= bl < m:
    #             if grid[bc][bl] != '#' and bvisited[bc][bl] == 0:#벽이 아니고 방문한적 있다면
    #                 while grid[bc][bl] != '#':
    #                     bvisited[bc][bl] = bvisited[bn[0]][bn[1]] + 1
    #                     bc += dd[0]
    #                     bl += dd[1]
    #                 blueq.append([bc,bl])
    # if rvisited[goal[0]][goal[1]] - 1 > 10 or rvisited[goal[0]][goal[1]] == 0:#10보다 크거나 도달 못했으면 실패
    #     print(-1)
    # elif rvisited[goal[0]][goal[1]] >= bvisited[goal[0]][goal[1]] and bvisited[goal[0]][goal[1]]: #파랑이 0이 아닐때 동시에 들어가거나 늦게 들어가도 실패
    #     print(-1)
    # elif rvisited[goal[0]][goal[1]] < bvisited[goal[0]][goal[1]]: #빨강이 먼저 도착.
    #     print(rvisited[goal[0]][goal[1]] - 1)
    # elif rvisited[goal[0]][goal[1]] - 1 <= 10 and bvisited[goal[0]][goal[1]] == 0:
    #     print(rvisited[goal[0]][goal[1]] - 1)
    # print(*rvisited,sep='\n')
    # print()
    # print(*bvisited, sep='\n')















