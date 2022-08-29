import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
구슬탈출! 1
빨간 구슬을 최소 10회 안에 탈출 시켜라!
파란 구슬이 먼저나오면 fail
1.최소? = bfs로가자
2.모든 경우를 다봐야하니까 bfs` 재귀로 해보자
--- 1시간 컷 실패. ㅠ
"""
if __name__ == "__main__":
    import sys
    from collections import deque
    r,sr=range,sys.stdin.readline
    n,m=map(int,sr().split())
    grid=[sr() for i in r(n)]
    for i in r(n):
        t1=grid[i].find('R')
        t2=grid[i].find('B')
        if t1>-1:red=[i,t1]
        if t2>-1:blue=[i,t2]
    #rvt=[[0 for _ in r(m)] for _ in r(n)]
    #bvt=[[0 for _ in r(m)] for _ in r(n)]
    vt= [[[[0 for _ in r(m)] for _ in r(n)] for _ in r(m)] for _ in r(n)]
    vt[red[0]][red[1]][blue[0]][blue[1]] = 1
    #rvt[red[0]][red[1]]=1
    #bvt[blue[0]][blue[1]]=1
    def incline(y,x,dy,dx):
        step=0
        while grid[y+dy][x+dx]!='#' and grid[y][x]!='O':
            x+=dx;y+=dy;step+=1
        return y,x,step
    q=deque([[red[0],red[1],blue[0],blue[1],0]]) #빨강,파랑 위치, 기울인 횟수
    to=[[1,0],[-1,0],[0,-1],[0,1]]  # 방향
    def bfs():
        while q:
            ry,rx,by,bx,inc=q.popleft()
            if inc+1>10:break#10번 넘어가면 실패
            for dy,dx in to:
                nry,nrx,rc=incline(ry,rx,dy,dx)
                nby,nbx,bc=incline(by,bx,dy,dx)
                if grid[nby][nbx]=='O':continue
                if grid[nry][nrx]=='O':print(1);return#빨강먼저 들어가면 1
                if (nry,nrx)==(nby,nbx): #구슬 겹치면 한놈 뒤로 빼기
                    if rc<bc:nby-=dy;nbx-=dx
                    else:nry-=dy;nrx-=dx
                if vt[nry][nrx][nby][nbx]^1: #not A or not B = not(A and B)/ rvt[nry][nrx]^1 or bvt[nby][nbx]^1
                    vt[nry][nrx][nby][nbx] = 1
                    #rvt[nry][nrx]=1 따로따로 visited를 하면 위치정보의 순서가 뒤바뀌어도 모름 두 visited를 곱한 형태여야함.
                    #bvt[nby][nbx]=1
                    q.append([nry,nrx,nby,nbx,inc+1])
        print(0)
    bfs()