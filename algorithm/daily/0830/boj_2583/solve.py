import sys
sys.stdin = open('input.txt')
"""
영역 구하기
앞의 그림이나 다른 영역문제와 비슷
직사각형 내부를 제외한 나머지 영역의 개수를 구하고
그 넓이도 구하시오
대신 사각형을 직접 칠해야한다.
"""
from collections import deque
R,C,k = map(int,input().split())
grid = [[1 for _ in range(C)] for _ in range(R)]
visited =[[0 for _ in range(C)] for _ in range(R)]
for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())# 시점 2, 끝점 2
    for y in range(y1,y2):
        for x in range(x1,x2): #실제와는 위아래 바뀌어서 그려지지만 ㄱㅊ
            grid[y][x] = 0 #사각형을 0으로 하자. 그래야 편함
to = [[1,0],[-1,0],[0,1],[0,-1]]
def check(i,j):
    q = deque([[i,j]])
    visited[i][j] = 1
    area = 0
    while q:
        area += 1
        y,x = q.popleft()
        for dy,dx in to:
            ny = y+dy ; nx = x+dx
            if 0<=ny<R and 0<=nx<C and visited[ny][nx] == 0 and grid[ny][nx] == 1:
                visited[ny][nx] = 1
                q.append([ny,nx])
    return area

ans = []
for i in range(R):
    for j in range(C):
        if visited[i][j] == 0 and grid[i][j] == 1:#방문 안한 여백부분
            temp = check(i,j) # C에서 반복되는 동안 다더하면 값이 합쳐짐
            ans.append(temp)
ans.sort()
print(len(ans)) #직사각형이 꽉채우는 경우가 없으므로 길이는 항상 1이상
print(*ans)





