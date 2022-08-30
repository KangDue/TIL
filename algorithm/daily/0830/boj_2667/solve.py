import sys
sys.stdin = open('input.txt')
"""
이전 영역구하기 문제랑 같음
단지번호 붙이기
주어진것
: 정사각형 모양의 지도
집이 있다면 1, 없으면 0
연결되었다 = 좌,우 위아래 연결디있다면 연결되있는 판정
이것도 사실 영역구하기 문제.
1. 집끼리 모두 연결 되어있는 단지수
2. 단지별 집의 수를 구하시오
"""

from collections import deque
def check(i,j):
    q = deque([[i,j]])
    visited[i][j] = 1
    c = 0
    qp=q.popleft
    qa=q.append
    while q:#while문의 반복수가 찾아간 노드의 수이다.
        c+=1
        y,x = qp()
        for dy,dx in to:
            ny = y+dy; nx = x + dx
            if 0<= ny < n and 0<=nx<n\
                    and visited[ny][nx] == 0 and grid[ny][nx] == 1:
                qa([ny,nx])
                visited[ny][nx] = 1
    return c
if __name__ =='__main__':
    n = int(input())
    grid = [[*map(int,input())] for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    to = [[1,0],[0,1],[-1,0],[0,-1]]
    ans = []
    ap = ans.append
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and grid[i][j] == 1:
                ap(check(i,j))
    ans.sort()
    print(len(ans))
    print(*ans,sep='\n')
    #별도로 단지가 없는경우, 전체가 한단지인 경우는 따로 없음.


