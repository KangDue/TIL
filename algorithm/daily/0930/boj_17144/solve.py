import sys
sys.stdin = open('input.txt')
"""
미세먼지 안녕
RxC 인 격자판
공기청정기는 항상 1번열에 있음
번호는 1번부터 시작. 크기는 두 행.(-1) 표시
r,c에는 먼지가 있고 먼지 양이 주어짐.
T초가 지난 후 남아있는 미세먼지 양
[작동순서]
<1. 먼지>
1. 미세먼지는 4방향으로 확산.
2. 인접 방향에 공기청정기 또는 칸이 없으면 확산 x
3. 확산되는 양은 5로 나눈 몫
4. 남은 양은 원래양 - (5로 나눈 몫)*확산된 방향의 수

<2. 공기청정기>
1. 위쪽 청정기는 반시계, 아래는 시계 방향으로 공기가 순환한다.
2. 바람이 불면 미세먼지가 바람 방향으로 모두 한칸씩 이동한다.
3. 공기청정기의 바람은 미세먼지가 없는 바람. 공기청정기로 들어가면 모두 정화됨.

#deque 까진 쓸거없이 먼지 정보만 받아서 추가  and 바람 ... 하면 될 듯?

TIP:
처음부터 조건을 잘 걸어야 한다.
범위를 세분화 해서 잘 걸러내야 이상한 error가 안남.
다양한 조건에 대해서 어떤 식으로 이들이 동작할 것인지 상상해보는 상상력도 필요하다.

##
나는 4000ms 걸렸는데 .ㅠ
랭킹권은 200대 
이양반들은 2차원을 1차원으로 flatten해서 풀었음.
and dict라 list등 저장 공간을 새로 교체하기 보다는 값을 교환하는 방식
나는 dict로 교체를 해버려서 시간을 많이 잡아먹었다.
다음에 다시 시간을 줄여보자!!
"""
import sys
input = sys.stdin.readline
R,C,T = map(int,input().split())
to = [[0,1],[0,-1],[1,0],[-1,0]]# 우, 상, 좌, 하
# print(R,C,T)
grid = [[*map(int,input().split())] for _ in range(R)]

dusts = dict()
ac = [] #공기 청정기 행 받기,
for i in range(R):
    for j in range(C):
        if grid[i][j] == -1:
            ac.append(i)
        elif grid[i][j]:
            dusts[(i, j)] = grid[i][j]
up,down = ac
"""
<upper half>
1. up 행은 모두 오른쪽으로 이동
2. 0행은 모두 왼쪽으로 이동
3. 0~up행까지 n-1열은 위로 이동
4. 0~up행까지 0열은 아래로 이동

<lower half>
1. down 행은 모두 오른으로 이동
2. n-1행은 모두 왼쪽으로 이동
3. down ~ n-1행까지 n-1열은 아래로 이동
4. down ~ n-1행까지 0열은 위로 이동
"""
# print(dusts)
# print(ac)
# print(*grid,sep='\n')

diffusion = dict()
#확산 & 청정기
for _ in range(T):
    for dust in dusts:
        each = dusts[dust] // 5
        y,x = dust
        if up-1 <= y <= down+1 and x == 0:  # 청정기에 가버리면 어차피 사라짐. , 청정기 위 아래로는 사라질 예정
            yy = -1
        elif up <= y <= down and 0 < x < C - 1:  # 우측 이동
            yy,xx = y,x+1
        elif (y == 0 or y == R - 1) and x > 0:  # 좌측 이동
            yy, xx = y, x - 1
        elif (x == C - 1 and down <= y < R-1) or (x == 0 and 0 <= y < up):  # 아래로 이동
            yy,xx = y+1, x
        elif (x == C - 1 and 0 < y <= up) or (x == 0 and down < y < R):  # 위로 이동
            yy,xx = y-1, x

        else:
            yy,xx = y,x
        if each:#아래 처럼 하면 확산시킨놈들은 바람따라 이동 하지만 원래 녀석들은 이동을 안함.
            for dy,dx in to:
                ny = y+dy; nx = x+dx
                if 0<=ny<R and 0<=nx<C: #유효범위
                    if (ny,nx) == (up,0) or (ny,nx) == (down,0): continue #청정기면 back
                    #날리면서 바람따라 이동시키자
                    if up <= ny <= down and 0 < nx < C-1: # 우측 이동
                        nx += 1
                    elif (ny == 0 or ny == R-1) and nx > 0: # 좌측 이동
                        nx -= 1
                    elif (nx == C-1 and down <= ny < R-1) or (nx == 0 and 0 <= ny < up): # 아래로 이동
                        ny += 1
                    elif (nx == C-1 and 0 < ny <= up) or (nx == 0 and down < ny < R): # 위로 이동
                        ny -= 1

                    if up<=ny<=down and nx==0: #청정기에 가버리면 어차피 사라지는데, 차감은 해야함.
                        dusts[dust] -= each
                        continue
                    if diffusion.get((ny,nx)):
                        diffusion[(ny, nx)] += each
                        dusts[dust] -= each  # 확산 한 만큼 감소
                    else:
                        diffusion[(ny,nx)] = each # 확산 dict 생성
                        dusts[dust] -= each # 확산 한 만큼 감소
        if yy != -1:
            if diffusion.get((yy, xx)):
                diffusion[(yy, xx)] += dusts[dust]  # 확산 먼지 이동후, 자기도 이동.
            else:
                diffusion[(yy, xx)] = dusts[dust]  # 확산 먼지 이동후, 자기도 이동.
    dusts,diffusion = diffusion, dict()
print(sum(dusts.values()))
# pic = [ [f'{0:2d}']*C for _ in range(R)]
# for pos,val in dusts.items():
#     pic[pos[0]][pos[1]] = f'{val:2d}'
# print(*pic,sep='\n')

