#피라미드 탐색
r = 2
c = 2
t = 2
n=5
ub = r - t if r - t >= 0 else 0
lb = r + t if r + t < n else n - 1
grid = [[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]]
for i in range(ub, lb + 1):
    d = t - abs(i - r)  # 좌우 거리
    if d == 0:
            print( grid[i][c] )
    else:  # 양 옆 탐색
        left = c - d
        right = c + d
        for j in (left, right):
            print(grid[i][j])


# def pyserch(r,c,s,e,t):#t초뒤 피라미드 탐색
#     global q,visited,time
#     temp = []
#     ub = r-t if r-t >= 0 else 0
#     lb = r+t if r+t <n else n-1
#     for i in range(ub,lb+1):
#         d = t-abs(i-r) #좌우 거리
#         if d == 0:
#             if 0 < grid[i][c] < s:#먹을수 있는 칸.
#                 grid[i][c] = 0
#                 visited = [[0 for _ in range(n)] for _ in range(n)]
#                 visited[i][c] = 1
#                 time = t + 1
#                 if e + 1 == s:  # 크기 커짐
#                     q = deque([[i, c, s + 1, 0, t + 1]])
#                 else:
#                     q = deque([[i, c, s, e + 1, t + 1]])
#                 return 1
#             elif grid[r][c] == s or grid[r][c]==0: #크기가 같으면 지나는 갈 수 있다.
#                 visited[r][c] = 1
#                 q.append([r,c,s,e,t+1])
#         else: #양 옆 탐색
#             left = c-d
#             right = c + d
#             for j in (left,right):
#                 if 0<=j<n and not visited[i][j]:
#                     if 0 < grid[i][j] < s:  # 먹을수 있는 칸.
#                         grid[i][j] = 0
#                         visited = [[0 for _ in range(n)] for _ in range(n)]
#                         visited[i][j] = 1
#                         time = t + 1
#                         if e + 1 == s:  # 크기 커짐
#                             q = deque([[i, j, s + 1, 0, t + 1]])
#                         else:
#                             q = deque([[i, j, s, e + 1, t + 1]])
#                         return 1