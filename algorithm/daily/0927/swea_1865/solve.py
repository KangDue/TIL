import sys
sys.stdin = open('input.txt')
"""
동철이의 일 분재
N명의 직원, 일이 N개
i번 직원이 j번 일을 하면 성공확률 p i,j
주어진 일이 모두 성공할 확률의 최댓값 구하기
"""

def check(r=0,tot=1):
    global maxv,grid,visited
    if r==n:
        maxv = max(maxv,tot)
        return 0
    if tot <= maxv:
        return 0
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            check(r+1,tot*grid[r][i]/100)
            visited[i] = 0

for t in range(int(input())):
    n = int(input())
    grid = [[*map(int,input().split())] for _ in range(n)]
    visited = [0]*n
    maxv = 0
    check()
    maxv = round(100*maxv,6)
    print(f'#{t+1} {maxv:.6f}')

    #print(*grid,sep='\n')