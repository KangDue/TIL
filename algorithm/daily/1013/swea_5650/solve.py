"""
핀볼게임 (NxN)
1 = 왼쪽 아래 삼각
2 = 왼쪽 위 삼각
3 = 오른쪽 위 삼각
4 = 오른쪽 아래 삼각
5 = 사각
6~10 = 웜홀
-1 = 블랙홀

공은 상하좌우
#수직/ 수평면 만나면 그대로 반대 방향
#경사면은 직각으로 꺾임.
#벽을 만나도 튕김.
#웜홀에 빠지면 다른 웜홀로 튀어나오고 방향은 그대로(같은 번호)
#블랙홀을 만나면 게임 끝남.
#출발위치로 돌아와도 게임 끝남.
#벽이나 블록에 부딪힐때 마다 점수 +
#출발위치, 진행방향 자유설정 가능, 점수 최대값은?
# 블록,웜홀,블랙홀 위치 제외

"""
import sys
to = [[-1,0],[1,0],[0,-1],[0,1]] #상하좌우 0123
sys.stdin = open('input.txt')

# 1은 반사 , 0는 수직
info = {1:{0:'r',1:'vr',2:'r',3:'vu'}, 2:{0:'r',1:'vr',2:'vd',3:'r'},
        3:{0:'r',1:'vl',2:'vd',3:'r'}, 4:{0:'v',1:'rl',2:'vu',3:'r'}}
rev = {0:1,1:0,2:3,3:2}

def dfs(y,x,d,score=0,end=0):#좌표1,2, 방향, 점수, 종료
    global maxv,n
    if not end:
        maxv = max(maxv,score)
        return 0
    else:
        ny,nx = y+to[d][0],x+to[d][1]
        if 0<=ny<n and 0<=nx<n:
            temp = grid[ny][nx]
            if temp == 1:
                if info[temp][d] =='r':
                    dfs(ny,nx,rev[d],score+1,end)
                elif info[temp][d] =='vu':
                    dfs(ny, nx, 0, score + 1, end)
                elif info[temp][d] =='vd':
                    dfs(ny, nx, 1, score + 1, end)
                elif info[temp][d] == 'vl':
                    dfs(ny, nx, 2, score + 1, end)
                elif info[temp][d] == 'vr':
                    dfs(ny, nx, 3, score + 1, end)
            elif temp == 2:
                if info[temp][d] =='r':
                    dfs(ny,nx,rev[d],score+1,end)
                elif info[temp][d] =='vu':
                    dfs(ny, nx, 0, score + 1, end)
                elif info[temp][d] =='vd':
                    dfs(ny, nx, 1, score + 1, end)
                elif info[temp][d] == 'vl':
                    dfs(ny, nx, 2, score + 1, end)
                elif info[temp][d] == 'vr':
                    dfs(ny, nx, 3, score + 1, end)
            elif temp == 3:
                if info[temp][d] =='r':
                    dfs(ny,nx,rev[d],score+1,end)
                elif info[temp][d] =='vu':
                    dfs(ny, nx, 0, score + 1, end)
                elif info[temp][d] =='vd':
                    dfs(ny, nx, 1, score + 1, end)
                elif info[temp][d] == 'vl':
                    dfs(ny, nx, 2, score + 1, end)
                elif info[temp][d] == 'vr':
                    dfs(ny, nx, 3, score + 1, end)
            elif temp == 4:
                if info[temp][d] =='r':
                    dfs(ny,nx,rev[d],score+1,end)
                elif info[temp][d] =='vu':
                    dfs(ny, nx, 0, score + 1, end)
                elif info[temp][d] =='vd':
                    dfs(ny, nx, 1, score + 1, end)
                elif info[temp][d] == 'vl':
                    dfs(ny, nx, 2, score + 1, end)
                elif info[temp][d] == 'vr':
                    dfs(ny, nx, 3, score + 1, end)
            elif temp == 5:
                dfs(ny,nx,rev[d],score+1,end)
            elif grid[ny][nx] == 6:
                # ny,nx = worm[e]
                # dfs()
                pass
            elif grid[ny][nx] == 0:
                dfs(ny,nx,d,score,1)
        else:#벽에 튕기면
            dfs(y, x, rev[d], score + 1, end)


for t in range(1,int(input())+1):
    n = int(input())
    grid = [[*map(int,input().split())] for _ in range(n)]
    print(*grid,sep='\n')
    maxv = 0
    bh = []
    wh = [[] for _ in range(12)]
    for i in range(n):
        for j in range(n):
            if 5 <= grid[i][j] <=10:
                wh[grid[i][j]].append([i,j])
            elif grid[i][j] == -1:
                bh.append([i,j])


    #
    # for i in range(n):
    #     for j in range(n):
    #         for d in range(4):

