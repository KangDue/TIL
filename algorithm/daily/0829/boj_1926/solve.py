import sys
sys.stdin = open('input.txt')
"""
그림의 개수와
가장큰 그림의 크리를 구하자
HOW?
:그림은 상하 또는 좌우로만 1로 연결된 경우이다.
-> 상하좌우 BFS 탐색을 하고 그와 동시에 카운트를 하며 visited 처리한다.(또는 지워버림)
"""
from collections import deque
R,C = map(int,input().split())
pic = [[*map(int,input().split())] for i in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
to = [[1,0],[0,1],[-1,0],[0,-1]]
def check(i,j):#i,j와 연결된 그림 찾기.
    area = 1#시작점
    q = deque([[i,j]])
    visited[i][j] = 1
    while q:
        y,x = q.popleft()
        for dy,dx in to:
            ny = y+dy; nx = x+dx
            if 0<= ny < R and 0<= nx < C and visited[ny][nx] == 0 and pic[ny][nx]:
                visited[ny][nx] = 1
                q.append([ny,nx])
                area += 1
    return area

count = 0
pic_size = []
for i in range(R):
    for j in range(C):
        if pic[i][j] and visited[i][j] == 0:
            count += 1
            pic_size.append(check(i,j))
print(count)
if count:print(max(pic_size))#그림이 하나도 없는 경우도 고려해야함.
else: print(0)



