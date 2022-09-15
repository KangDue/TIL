import sys
sys.stdin = open('input.txt')
"""
NxN 격자의 정사각형 방
grid[i][j]에는 1 이상 N^2 이하의 수 Aij가 있다. 모든 방의 숫자는 다름.
당신은 방에서 상하좌우로 이동 가능하지만, 다음방의 숫자가 현재 방보다 정확히 1 커야함
어디서 시작해야 가장 많이 이동가능한가?
테스트케이스 27개
시간초과 뜨는데 가지치기 해줘야할듯.
"""
from collections import deque
to = [[1,0],[-1,0],[0,1],[0,-1]]
def check(r,c): #갈수 있는 길이를 업데이트 하자! 매번 새로할필요가 없음.
    q = deque([[r,c]])
    visited[r][c] = 1
    while q:
        y,x = q.popleft()
        for dy,dx in to:
            ny = y+dy; nx = x + dx
            if ny//n-1 and nx//n-1 and not visited[ny][nx] and grid[ny][nx]==grid[y][x]+1:
                visited[ny][nx] = visited[y][x] + 1
                q.append([ny,nx])
    return [grid[r][c],visited[y][x]]#마지막으로 간 노드까지 가는 거리

for t in range(int(input())):
    n = int(input())
    grid = [[*map(int,input().split())] for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    #탐색을 숫자가 작은순으로 해줘야함.
    #겹칠경우 가장 낮은 방번호를 출력해야하기때문.
    sg = []
    for i in range(n):
        for j in range(n):
           sg.append([grid[i][j],i,j])
    sg.sort()
    temp=[]
    for v,r,c in sg:
        if not visited[r][c]:
            temp.append(check(r, c))
    temp.sort(key=lambda x:(x[1],-x[0]))
    print(f'#{t+1}',*temp[-1])
