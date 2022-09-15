import sys
sys.stdin = open('input.txt')
"""
미생물격리
1. 정사각형 구역 안에 미생물 존재 (K마리)
2. NxN 정사각형은 테두리부분은 특수 약품처리(미생물 x)
3. 최초 각 군집의 위치y 위치x, 군집내 미생물 수, 이동 방향 주어짐
4. 한 스텝마다 이동
5. 약품에 닿으면 절반이 죽고 이동방향이 반대로 바뀜.
6. 살아남은 미생물 수는 원래 수 / 2 에소 소수점 버린값 = 2로 나눈 몫
7. 1마리가 벽에닿으면 사라짐
8. 군집이 서로 만나면 합쳐지며 숫자도 합쳐짐.이동 방향은 미생물 수가
가장 많은 군집의 이동방향, (같은 경우는 없음)
9. M시간 후 남아있는 미생물 수의 총합을 구하여라 
"""
# from collections import defaultdict as dd
# from itertools import accumulate as ac
# to = [0,[-1,0],[1,0],[0,-1],[0,1]] #상 하 좌 우
# rev = {1:2,2:1,3:4,4:3}
# for t in range(int(input())):
#     N,M,K = map(int,input().split()) #한 변에 있는  셀의 개수 N, 격리 시간 M, 미생물 군집의 개수 K
#     #초기화 작업(보기 편하게)
#     grid = [[[-1,-1] for _ in range(N)] for _ in range(N)]
#
#     for i in range(1,N-1):
#         for j in range(1,N-1):
#             grid[i][j] = [0,0]
#     aos = []
#     #입력 받아오기
#     for _ in range(K):
#         y,x,ea,direct = map(int,input().split())
#         grid[y][x]=[ea,direct]
#         aos.append([y,x,ea,direct])
#     # print(aos)
#     # print(*grid,sep='\n')
#     while M:
#         visit = dd(list)
#         for o in range(len(aos)):
#             y,x,ea,direct = aos[o]
#             if ea == 0:continue #죽었다면 볼 필요 없다.
#             ny = y + to[direct][0]; nx = x + to[direct][1]
#             if ny == 0 or ny == N-1 or nx == 0 or nx == N-1:#약품에 닿으면 #범위를 잘보자.. N이 아니라  N-1
#                 aos[o][2] //=2 #줄이고
#                 aos[o][3] = rev[direct] #방향전환
#             aos[o][0] = ny #이동 1
#             aos[o][1] = nx #이동 2
#             visit[(ny,nx)].append(o) # 이동한 위치 저장
#         for key,values in visit.items():
#             if len(values) > 1: #2개 이상 만났다면
#                 mv = max(values,key=lambda x:aos[x][2])#가장 큰 군집 번호
#                 easum = 0
#                 for each in values:
#                     easum += aos[each][2]
#                     aos[each][2] = 0 #0으로 만들면 알아서 이제 걸러짐.
#                 aos[mv][2] = easum #가장 큰놈 따라감.
#         M-=1
#     #print(*aos,sep='\n')
#     print(f'#{t+1} {sum(map(lambda x:x[2],aos))}')



## 제출용!
R,I,W=range,int,input
from collections import defaultdict as dd
to = [0, [-1, 0], [1, 0], [0, -1], [0, 1]]  # 상 하 좌 우
rev = {1: 2, 2: 1, 3: 4, 4: 3}
for t in R(I(W())):
 N,M,K=map(I,W().split());aos=[]
 for _ in R(K):
  y,x,ea,di= map(I,W().split());aos.append([y, x, ea, di])
 while M:
  v=dd(list);M-=1
  for o in R(len(aos)):
   y,x,ea,di=aos[o]
   if not ea:
    continue
   ny=y+to[di][0];nx=x+to[di][1]
   if (ny+1)%N<2 or (nx+1)%N<2:
    aos[o][2]//=2;aos[o][3]=rev[di]
   aos[o][0:2]=[ny,nx]
   v[(ny,nx)].append(o)
  for k in v:
   if len(v[k])>1:
    mv=max(v[k],key=lambda x:aos[x][2])
    es=0
    for ch in v[k]:
     es+=aos[ch][2];aos[ch][2]=0
    aos[mv][2]=es
 print(f'#{t+1} {sum(map(lambda x:x[2],aos))}')
