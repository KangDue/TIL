import sys
sys.stdin = open('input.txt')
"""
최소 생산비용
N종의 제품을 N 곳의 공장에서
한 곳당 한가지씩 생산
전체 제품의 최소 생산 비용 계산
"""
def check(r=0,tot=0):
    global minv
    if r==n:
        minv = min(minv,tot)
        return 0
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            if tot + costs[r][i] < minv:
                check(r+1,tot+costs[r][i])
            visited[i] = 0

for t in range(int(input())):
    n = int(input())
    costs = [[*map(int,input().split())] for _ in range(n)]
    visited = [0] * n
    minv = 1500
    check()
    print(f'#{t+1} {minv}')