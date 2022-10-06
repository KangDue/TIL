"""
벽부수고 이동하기 3
시작은 낮이고
낮 밤이 한 스텝마다 번갈아 가면서 간다.
멈춰서 같은칸에 머물러도 바뀐다.(애초에 가만히 있나??)
벽은 낮에만 부술수 있다. -> 낮을 기다렸다가 벽을 부수고 가는게 이득일 수도 있다.
범위를 확실하게 나누고 step을 한번에 관리하는 방식이 굉장히 유용한듯 하다.
bfs랑 좀더 맞는 느낌.
"""
import sys
sys.stdin = open('input.txt')
R,C,K = map(int,input().split())
grid = [-1]*(C+2) + sum([[-1]+[*map(int,input())]+[-1] for _ in range(R)],[])+[-1]*(C+2)
C+=2

GOAL = (R+1)*C -2 # 도착지

INF = int(1e9)
visited = [INF]*C
for i in range(R):
    visited += [INF] + [0]*(C-2) + [INF] #좌우 패딩
visited += [INF]*C

#시작점을 벽을 깬 횟수로 하는데 왜 2로할까???
visited[C+1] = INF#둘 째 행의 둘째 열 = 시작 점.

q = [(C+1,K+1)]# 시작점, 벽을 깰 수 있는 횟수
step = 1 #step
mode = 1 # 1은 낮, 0은 밤.
while visited[GOAL] == 0 and q:
    new = []
    for pos,can in q:
        if visited[pos-1] < can:
            if not mode and grid[pos-1]: #밤 이고 벽일때 만 pass
                pass
            else:
                visited[pos-1] = can
                new.append((pos-1,can-grid[pos-1])) # grid가 벽이어야 1빼고 아니면 그대로

        if visited[pos+1] < can:
            if not mode and grid[pos+1]: #밤 이고 벽일때 만 pass
                pass
            else:
                visited[pos+1] = can
                new.append((pos+1,can-grid[pos+1]))

        if visited[pos-C] < can:
            if not mode and grid[pos-C]: #밤 이고 벽일때 만 pass
                pass
            else:
                visited[pos-C] = can
                new.append((pos-C,can-grid[pos-C]))

        if visited[pos+C] < can:
            if not mode and grid[pos+C]: #밤 이고 벽일때 만 pass
                pass
            else:
                visited[pos+C] = can
                new.append((pos+C,can-grid[pos+C]))
        if not mode: #밤이면 대기하는거 추가
            visited[pos] = can
            new.append((pos, can))
    step += 1
    q = new
    mode = not mode

if not visited[GOAL]:
    print(-1)
else:
    print(step)