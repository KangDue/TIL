import sys
sys.stdin = open('input.txt')
"""
체스판에서 나이트가 이동하는데
최소 몇번만에 목적지에 닿을 수 있나 ?
문제 설명을 보니 도달못하는 경우는 없는 듯 하다.
"""
from collections import deque
for t in range(int(input())):
    n = int(input())
    sy,sx = map(int,input().split()) #어차피 정사각이라 받는 y,x 순서 상관 없음
    ey,ex = map(int,input().split())
    to = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]#8방향 가능
    visited = [[0 for _ in range(n)] for _ in range(n)]
    q=deque([[sy,sx,0]])#y,x,step
    visited[sy][sx] = 1
    while q:
        y,x,time = q.popleft()
        if [y, x] == [ey, ex]:#체크를 여기서해야 첫값이 도착지인 경우도 catch 함.
            print(time);break

        for dy,dx in to:
            ny = y+dy; nx = x+dx
            if 0<= ny <n and 0<= nx <n and visited[ny][nx]==0:
                q.append([ny,nx,time+1])
                visited[ny][nx] = 1



