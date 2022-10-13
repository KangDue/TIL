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

sys.stdin = open('input.txt')

# 1은 반사 , 0는 수직
info = {1:{0:'r',1:'vr',2:'vu',3:'r'}, 2:{0:'vr',1:'r',2:'vd',3:'r'},
        3:{0:'vl',1:'r',2:'r',3:'vd'}, 4:{0:'r',1:'vl',2:'r',3:'vu'}}
rev = {0:1,1:0,2:3,3:2}
to = [[-1,0],[1,0],[0,-1],[0,1]] #상하좌우 0123

for t in range(1,int(input())+1):
    n = int(input())
    grid =[[5]*(n+2)] + [[5]+[*map(int,input().split())]+[5] for _ in range(n)] + [[5]*(n+2)]
    maxv = 0
    wh = [[] for _ in range(12)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if grid[i][j]:
                if 6 <= grid[i][j] <=10:
                    wh[grid[i][j]].append((i,j))
    whinfo = {}
    for li in wh:
        if li:
            whinfo[li[0]] = li[1]
            whinfo[li[1]] = li[0]

    # dfs(i, j, d, (i, j))
    for i in range(1,n+1):
        for j in range(1,n+1):
            if not grid[i][j]:
                for direction in range(4):
                    stack = [[i,j,direction,0]]
                    visited = [[0 for _ in range(n+2)] for _ in range(n + 2)]
                    start = 0
                    while stack:
                        y,x,d,score = stack.pop()
                        if start and y==i and x==j:
                            maxv = max(maxv, score)
                            break
                        start = 1
                        ny, nx = y + to[d][0], x + to[d][1]
                        if 1 <= ny <= n and 1 <= nx <= n:
                            temp = grid[ny][nx]
                            if 1 <= temp <= 4:
                                if info[temp][d] == 'r':
                                    stack.append([ny,nx,rev[d],score+1])
                                elif info[temp][d] == 'vu':
                                    stack.append([ny,nx,0,score+1])
                                elif info[temp][d] == 'vd':
                                    stack.append([ny,nx,1,score+1])
                                elif info[temp][d] == 'vl':
                                    stack.append([ny,nx,2,score+1])
                                elif info[temp][d] == 'vr':
                                    stack.append([ny,nx,3,score+1])
                            elif temp == 5:
                                stack.append([ny,nx,rev[d],score+1])
                            elif temp == -1:
                                maxv = max(maxv, score)
                                break
                            elif temp:  # 웜홀
                                ny, nx = whinfo.get((ny, nx))
                                stack.append([ny,nx,d,score])
                            else:  # 0인 곳,
                                stack.append([ny,nx,d,score])
                        else:  # 벽에 튕기면
                            stack.append([ny,nx,rev[d],score+1])

    print(f'#{t} {maxv}')




