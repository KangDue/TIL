"""
확장 게임


"""
import sys
sys.stdin = open('input.txt')
R,C,P = map(int,input().split()) # 행, 열, 플레이어 수
per = [0]+[*map(int,input().split())]
grid = [-1]*(C+2) + sum([[-1]+[*input()]+[-1] for _ in range(R)],[])+[-1]*(C+2)
C+=2
player={i:[] for i in range(1,P+1)}

visited = [-1]*C
for i in range(R):
    visited += [-1] + [0]*(C-2) + [-1] #좌우 패딩
visited += [-1]*C
print(per)
print(grid)
for i in range(len(grid)):
    if type(grid[i])==str and grid[i].isdecimal():
        grid[i] = int(grid[i])
        player[grid[i]].append(i)
print(player)
#
# q = [(C+1,K+1)]# 시작점, 벽을 깰 수 있는 횟수
# step = 1 #step
# mode = 1 # 1은 낮, 0은 밤.
# while visited[GOAL] == 0 and q:
#     new = []
#     for pos,can in q:
#         if visited[pos-1] < can:
#             if not mode and grid[pos-1]: #밤 이고 벽일때 만 pass
#                 pass
#             else:
#                 visited[pos-1] = can
#                 new.append((pos-1,can-grid[pos-1])) # grid가 벽이어야 1빼고 아니면 그대로
#
#         if visited[pos+1] < can:
#             if not mode and grid[pos+1]: #밤 이고 벽일때 만 pass
#                 pass
#             else:
#                 visited[pos+1] = can
#                 new.append((pos+1,can-grid[pos+1]))
#
#         if visited[pos-C] < can:
#             if not mode and grid[pos-C]: #밤 이고 벽일때 만 pass
#                 pass
#             else:
#                 visited[pos-C] = can
#                 new.append((pos-C,can-grid[pos-C]))
#
#         if visited[pos+C] < can:
#             if not mode and grid[pos+C]: #밤 이고 벽일때 만 pass
#                 pass
#             else:
#                 visited[pos+C] = can
#                 new.append((pos+C,can-grid[pos+C]))
#         if not mode: #밤이면 대기하는거 추가
#             visited[pos] = can
#             new.append((pos, can))
#     step += 1
#     q = new
#     mode = not mode
#
# if not visited[GOAL]:
#     print(-1)
# else:
#     print(step)