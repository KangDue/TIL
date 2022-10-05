"""
다리만들기
한 섬과 다른 섬을 잇는 다리를 최소 비용으로 만든다.
영영찾기 비슷
각 섬들중 아무거나 2개를 잇는 최단 경로길이 구하기
처음 주어지는 지도는 땅이 1로 표시됨. (nxn) 지도

"""
def manh(x,y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1]) -1
from itertools import combinations as cb
from collections import deque
o = open('input.txt')
n = int(next(o))
grid = [[*map(int,next(o).split())] for _ in range(n)]
visited = [[0]*n for _ in range(n)]
to = [[1,0],[-1,0],[0,1],[0,-1]]
edges=[]
for i in range(n):
    for j in range(n):
        if grid[i][j] and not visited[i][j]:
            temp = []
            q = deque([[i,j]])
            visited[i][j] = 1
            while q:
                y,x = q.popleft()
                for dy,dx in to:
                    ny = y+dy; nx = x + dx
                    if 0<=ny<n and 0<=nx<n and not visited[ny][nx]:
                        if grid[ny][nx]:
                            visited[ny][nx] = 1
                            q.append([ny, nx])
                        else:#0과 붙어있는 edge는 따로 모으기
                            temp.append([y,x])
            edges.append(temp)
minv = int(1e9)
for a,b in cb(edges,2):
    for i in a:
        for j in b:
            minv = min(minv,manh(i,j))
print(minv)
# print(*edges,sep='\n')




