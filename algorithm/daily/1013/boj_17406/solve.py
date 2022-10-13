"""
NxM 배열이 주어질 때
각 행의 합중 최소값이 그 행의 값
회전연산이 있다.
1번부터 시작임.
r,c,s 좌상이 r-s,c-s, / 우하 r+s,c+s 인 정사각형을 시계 방향으로 한 칸씩 돌린다.
"""
import sys
sys.stdin = open('input.txt')
from itertools import permutations as pm
def rotate(r,c,s,grid): #한 껍데기 씩 회전시키자.
    #c-s ~ c+s
    while s:
        temp = []
        for i in range(c-s,c+s+1): #윗줄 횡단
            temp.append(grid[r-s][i])
        for i in range(r-s+1,r+s): #왼쪽 줄
            temp.append(grid[i][c+s])
        for i in range(c+s,c-s-1,-1): #아래 줄
            temp.append(grid[r+s][i])
        for i in range(r+s-1,r-s,-1): #오른쪽 줄
            temp.append(grid[i][c-s])
        rot = [temp.pop()] + temp
        rot.reverse()
        for i in range(c - s, c + s + 1):  # 윗줄 횡단
            grid[r - s][i] = rot.pop()
        for i in range(r - s+1, r + s):  # 왼쪽 줄
            grid[i][c + s] = rot.pop()
        for i in range(c + s, c - s - 1, -1):  # 아래 줄
            grid[r + s][i] = rot.pop()
        for i in range(r + s - 1, r - s, -1):  # 오른쪽 줄
            grid[i][c - s] = rot.pop()
        s -= 1

R,C,K = map(int,input().split())
grid = [[-1]*(C+1)]+[[-1]+[*map(int,input().split())] for _ in range(R)]
order = []
for _ in range(K):
    order.append([*map(int, input().split())])
# print(*grid,sep='\n')
minv = int(1e9)
for permu in pm(order,K):#순열 돌려야함. 주어진 순서대로 수행이 아니라, 맘대로 조작임
    ngrid = [[grid[i][j] for j in range(C+1)] for i in range(R+1)]
    for rt in permu:
        rotate(*rt,ngrid)
    for i in range(1,R+1):
        minv = min(sum(ngrid[i][1:]),minv)
print(minv)
