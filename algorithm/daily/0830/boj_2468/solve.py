import sys
sys.stdin = open('input.txt')
"""
(앞의 영역 구하기들에서 조건하나 추가된 간단한 문제?) 가 아니네
- 비의 양의따라 변하는 안전영역의 개수중 최대값을 찾아라!
안전 영역
비가 많이 내렸을때 물에 잠기지 않는 안전한 영역이 최대 몇개인가?
내리는 비의 양에 따라 일정 높이 이하의 모든 지점이 물에 잠긴다.
지역의 높이 정보가 담긴 행렬을 준다.(정사각)
서로 상하좌우로 인접한 곳이 하나의 안전 영역이다.
!! 영역의 개수만 알면됨, 영역의 넓이까진 필요 x
"""
from collections import deque
n = int(input())
grid = [[*map(int,input().split())] for _ in range(n)]
flat =  list(set(sum(grid,start=[])))
#비의 양 이하인 지점은 전부 잠긴다.
#최대값이면 싹다 잠기니까 필요 없다.
flat.remove(max(flat))
#이 중복없는 높이에 존재하는 값들로 안전구역 을 나눠볼 수 있다.
#모든 비의양 범위 순회는 비 효율적이다.

to = [[1,0],[-1,0],[0,1],[0,-1]]
def check(i,j):
    global pivot
    q = deque([[i,j]])
    visited[i][j] =1
    while q:
        y,x = q.popleft()
        for dy,dx in to:
            ny = y+dy; nx = x + dx
            if 0<= ny <n and 0<=nx<n and visited[ny][nx]==0\
                and grid[ny][nx] > pivot: #pivot 이하가 물에 잠기니까 안잠긴 영역 찾아야함
                q.append([ny,nx])
                visited[ny][nx] = 1


maxv = 1#모두 높이가 같을때 안전영역이 최소 하나이다.
for pivot in flat:#각 기준마다 visited 초기화 해줘야함
    c = 0 #높이별 비교 해줘야함
    visited = [[0 for _ in range(n)] for _ in range(n)]  # 여러번 반복해야함
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0 and grid[i][j] > pivot:
                c+=1#영역별 추가
                check(i,j)
    maxv = max(maxv,c)
print(maxv)

# print(*visited, sep='\n')
# print("-----", pivot, c)
# print(*grid, sep='\n')
# print()