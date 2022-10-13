"""
다리는 직선으로만 연결하고,
다리의 길이는 2 이상이어야 하다.
다리가 겹쳐도 별개로 본다.
"""
import sys
sys.stdin = open('input.txt')


from collections import deque
to = [[1,0],[-1,0],[0,1],[0,-1]]
R,C = map(int,input().split())
grid = [[*map(int,input().split())] for _ in range(R)]
group = [[] for _ in range(6)]
visited = [[0 for _ in range(C)] for _ in range(R)]
idx = 0
for i in range(R):
    for j in range(C):
        if grid[i][j] and not visited[i][j]:
            idx += 1
            q = deque([[i,j]])
            visited[i][j] = 1
            while q:
                y,x = q.popleft()
                for dy,dx in to:
                    ny,nx=y+dy,x+dx
                    if 0<=ny<R and 0<=nx<C and not visited[ny][nx]:
                        visited[ny][nx] = 1
                        q.append([ny,nx])
                        group[idx].append([ny,nx])
print(group)