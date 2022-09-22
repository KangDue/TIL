import sys
sys.stdin = open('input.txt')
"""
벌꿀채취
NxN 벌통 각 꿀 칸에는 꿀이있고
두명의 일꾼으로 벌꿀채취 최대로
각각 가로로 M개의 칸을 선택 , 서로 겹치면 안됨.
수익은 채취한 각 꿀의 제곱합.
채취할 수 있는 최대 양이 정해져있음.
"""
from itertools import combinations as cb
def sur(arr):
    global c
    mv = 0
    for i in range(len(arr),0,-1):
        for comb in cb(arr,i):
            temp = sum(comb)
            if temp <= c:
                mv = max(mv,sum(map(lambda x:x*x,comb)))
    return mv
def sell(grid):
    global maxv
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n-m+1):
            s1 = grid[i][j:j+m]
            visited[i][j:j+m] = [1]*m
            for a in range(n):
                for b in range(n - m + 1):
                    if 1 not in visited[a][b:b + m]:
                        s2 = grid[a][b:b + m]
                        maxv = max(maxv,sur(s1)+sur(s2))
            visited[i][j:j + m] = [0] * m

for t in range(int(input())):
    n,m,c = map(int,input().split())
    grid = [[*map(int,input().split())] for _ in range(n)]
    maxv=0
    sell(grid)
    print(f'#{t+1} {maxv}')