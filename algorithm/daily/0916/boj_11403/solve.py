import sys
sys.stdin = open('input.txt')
"""
무가중치 무향그래프 G
모든 정점(i,j)에 대해 i,j 경로가 있나 없나 구해보자.
인접행렬에 플로이드 워셜 알고리즘을 갈기자.
"""
n = int(input())
grid = [input().split() for i in range(n)] #인접행렬이라 걍 쓰면됨
for k in range(n):
    for i in range(n):
        for j in range(n):
            if grid[i][k] == '1' and grid[k][j] == '1':
                grid[i][j] = '1'
for i in grid:
    print(*i)