"""
다리는 직선으로만 연결하고,
다리의 길이는 2 이상이어야 하다.
다리가 겹쳐도 별개로 본다.
10분
예제 그림이 정답인줄알고 ; 계속 왜 안되나 했네 아오
1시간 33분 합격이긴 한데
예제그림 낚인시간 고려
1시간 10분 컷.
"""
import sys
sys.stdin = open('input.txt')

def check(p1,p2):#방해물 있는지 체크
    y1,x1 = p1
    y2,x2 = p2
    if x1==x2  and abs(y1-y2) > 2:#vert
        if y1 > y2:
            for i in range(y2+1,y1):
                if grid[i][x1]:
                    return 0,0
            return 1,abs(y1-y2)-1
        else:
            for i in range(y1+1,y2):
                if grid[i][x1]:
                    return 0,0
            return 1,abs(y1-y2)-1
    if y1==y2 and abs(x1-x2) > 2:#horizon
        if x1 > x2:
            for i in range(x2+1,x1):
                if grid[y1][i]:
                    return 0,0
            return 2,abs(x1-x2)-1
        else:
            for i in range(x1+1,x2):
                if grid[y1][i]:
                    return 0,0
            return 2,abs(x1-x2)-1
    return 0,0

from collections import deque
to = [[1,0],[-1,0],[0,1],[0,-1]]
R,C = map(int,input().split())
grid = [[*map(int,input().split())] for _ in range(R)]
group = [[] for _ in range(7)]
visited = [[0 for _ in range(C)] for _ in range(R)]
idx = 0
edges = []
for i in range(R):
    for j in range(C):
        if grid[i][j] and not visited[i][j]:
            idx += 1
            q = deque([[i,j]])
            visited[i][j] = idx
            group[idx].append([i,j])
            while q:
                y,x = q.popleft()
                for dy,dx in to:
                    ny,nx=y+dy,x+dx
                    if 0<=ny<R and 0<=nx<C and not visited[ny][nx] and grid[ny][nx]:
                        visited[ny][nx] = idx
                        q.append([ny,nx])
                        group[idx].append([ny,nx])

for i in range(1,6):
    for j in range(i+1,7):
        hd = 1<<20
        vd = 1<<20
        for p1 in group[i]: #섬 1
            for p2 in group[j]: #섬 2
                kind,dist = check(p1,p2)
                if kind==1:
                    hd = min(hd,dist)
                elif kind==2:
                    vd = min(vd,dist)

        if 2<= hd < 1<<20:
            edges.append([i,j,hd])
        if 2<= vd < 1<<20:
            edges.append([i, j, vd])

parent = [i for i in range(7)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    else:
        return x
def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
        for i in range(7):
            if parent[i] == y:
                parent[i] = x
    else:
        parent[x] = y
        for i in range(7):
            if parent[i] == x:
                parent[i] = y
edges.sort(key = lambda x:x[2],reverse=True)

n = 0
for i in range(7):
    if group[i]:
        n+=1
mst = []
mstv = 0

while len(mst) != n-1:
    try:
        x,y,d = edges.pop()
        if parent[x] != parent[y]:
            union(x,y)
            mstv += d
            mst.append([x,y,d])
    except:
        print(-1)
        break
else:
    print(mstv)
