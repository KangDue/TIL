import sys
sys.stdin = open('input.txt')
"""
N-queen
N*N 보드에 N개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수는 몇가지가 있을까?
N이 주어졌을 때, 퀸을 놓는 방법의 수
"""
def check(grid, i, j):
    temp = [[grid[i][j] for j in range(n)] for i in range(n)]
    temp[i][j] = 1
    for r in range(i + 1, n):
        gap = r-i
        temp[r][j] = 1
        if j - gap >= 0:  temp[r][j - gap] = 1
        if j + gap < n: temp[r][j + gap] = 1
    return temp

for t in range(int(input())):
    n = int(input())
    ans = 0
    if n == 1: ans = 1
    elif n == 2: ans = 0
    else:
        grid = [[0]*n for i in range(n)]
        def counts(grid,row=0):
            global n,ans
            if row == n:ans += 1;return 0
            for i in range(n):
                if not grid[row][i]:
                    counts(check(grid,row,i),row+1)
        counts(grid)
        # print(*check(grid,0,p2),sep='\n')
    print(f'#{t+1} {ans}')





