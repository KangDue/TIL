import sys
sys.stdin = open('input.txt')
"""
치즈는 냉동보관해야 하는데 
실온에 두어서 녹고있다.
2변 이상이 공기와 접촉죽인 치즈는 한시간 뒤에 녹아 사라진다.
치즈 내부의 빈공간은 제외.
치즈가 모두 녹아 없어지는데 걸리는 시간은?
"""
#외부 공기는 가장 바깥 격자부터 bfs로 닿는 범위 전부임.
#나머지는 내부.
#외부에서 시작해서 지속적으로 공격하는건 어떨까? 는 아닌듯 ㅋ; 치즈 녹는 조건 구하기 힘듬
from collections import deque
n,m = map(int,input().split())
grid = [[*map(int,input().split())] for _ in range(n)]
# print(*grid,sep='\n')
visited = [[0]*m for _ in range(n)]
to = [[1,0],[-1,0],[0,1],[0,-1]]
# print("---------")
q = deque([[0,0]])
while q:
    y,x = q.popleft()
    for dy,dx in to:
        ny = y+dy; nx = x+dx
        if 0<=ny<n and 0<=nx<m and not visited[ny][nx] and not grid[ny][nx]:
            visited[ny][nx] = -1
            q.append([ny,nx])
cheese = dict()
for r in range(n):
    for c in range(m):
        if not visited[r][c] and grid[r][c]:
            cheese[(r,c)] = 1
time = 0
while cheese:
    time += 1
    temp = []
    for y,x in cheese:
        contact = 0
        for dy,dx in to:
            ny = y+dy; nx = x+dx
            if visited[ny][nx] == -1:
                contact += 1
        if contact > 1:
            temp.append((y,x))
    for i in temp:
        visited[i[0]][i[1]] = -1
        cheese.pop(i)
print(time)