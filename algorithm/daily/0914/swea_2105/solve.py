import sys
sys.stdin = open('input.txt')
"""
디저트카페투어 nxn 지역에 카페가 있다.
숫자는 해당 카페에서 파는 디저트 종류.
대각선으로만 1칸씩 이동 가능하다.
무조건 사각형 모양으로 움직이며 원위치로 다시 돌아와야 한다.
투어중에 같은 숫자의 디저트 가게가 있으면 안된다.
사각형 한변의 길이는 1이상, (한군데만 가기 x)
사각형을 못만들고 선으로만 이동도 못함.
임의의 한지점에서 출발해서 돌아올때 가장 많이 먹는 경우 구하기
못 먹는 경우는 -1

"""
# from collections import defaultdict
# from itertools import product as pr
# #컨티뉴 조건때문에 runtime 에러 뜨다가 고치니까 정상작동
# def tour(r,c):
#     global mv
#     for a,b in shapes: #각 모양별
#         h = defaultdict(I)
#         h[grid[r][c]] = 1
#         ny,nx=r,c
#         if c+a < n and c-b > -1 and r + a + b < n: #가능한 범위
#             for i in R(a):
#                 ny += to[0][0]; nx += to[0][1]
#                 if h.get(grid[ny][nx]):break
#                 h[grid[ny][nx]] = 1
#             else:
#                 for i in R(b):
#                     ny += to[1][0]; nx += to[1][1]
#                     if h.get(grid[ny][nx]):break
#                     h[grid[ny][nx]] = 1
#                 else:
#                     for i in R(a):
#                         ny += to[2][0]; nx += to[2][1]
#                         if h.get(grid[ny][nx]):break
#                         h[grid[ny][nx]] = 1
#                     else:
#                         for i in R(b-1):#마지막칸은 갈 필요 없음.
#                             ny += to[3][0]; nx += to[3][1]
#                             if h.get(grid[ny][nx]):break
#                             h[grid[ny][nx]] = 1
#                         else: mv = max(mv,len(h)-1)
#     return mv
# for t in R(I(W())):
#     n = I(W())
#     grid = [[*map(I,W().split())] for _ in R(n)]
#     to = [[1, 1],[1, -1], [-1, -1], [-1, 1]]#1 2 3 4 돌면 최소단위 사각형
#     shapes = list(pr(R(1,n-1),repeat=2)) #생성가능한 사각형 형태
#     #홀수번 째 칸에서만 사각형 시작 가능 ( 열조건 )
#     #마지막 행 - 2칸째 까지만 사각형 시작 가능. ( 행 조건 )
#     #shape의 합 = 아래로 가는 칸수 shape[0] = 오른쪽으로 가는 칸수
#     #shape[1] 왼쪽으로 가는 칸수, 이 3가지 고려해서
#     #shape 필터링
#     #또한 같은 숫자를 만나면 종료, max와의 접근가능성 비교까지 하면 너무 많아짐.
#     mv = 0
#     for r in R(n-2): #행조건
#         for c in R(1,n-1): #열조건
#             tour(r, c)
#     if not mv:mv=-2
#     prI(f'#{t+1} {mv+1}')


R,I,W=range,int,input
from collections import defaultdict as dd
def tour(r,c):
    global mv
    for a,b in iter((a,b) for b in R(1,c+1) for a in R(1,n-c) if a+b<n-r):
        h=dd(I);h[grid[r][c]]=1;ny,nx=r,c;s=(a,b,a,b-1)
        for dy,dx in (to[i] for i in R(4) for _ in R(s[i]) if s[i]):
            ny+=dy;nx+=dx
            if h.get(grid[ny][nx]):break
            h[grid[ny][nx]]=1
        else:mv=max(mv,len(h)-1)
    return mv
for t in R(I(W())):
    n=I(W());grid=[[*map(I,W().split())] for _ in R(n)];to=[[1,1],[1,-1],[-1,-1],[-1,1]];mv=0
    for r in R(n-2):
        for c in R(1,n-1):
            tour(r, c)
    if not mv:mv=-2
    print(f'#{t+1} {mv+1}')