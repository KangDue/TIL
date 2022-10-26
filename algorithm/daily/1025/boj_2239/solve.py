import sys
sys.stdin = open('input.txt')
grid = [[0]*10] + [[0]+[*map(int,input())] for _ in range(9)]
print(*grid,sep='\n')
print("----")
nums = list(range(10))
square_visited = [[0]*10 for _ in range(10)]
col_visited = [[0]*10 for _ in range(10)]
row_visited = [[0]*10 for _ in range(10)]
for i in range(1,10):
    for j in range(1,10):
        if grid[i][j]:
            row_visited[i][grid[i][j]] = 1
            col_visited[j][grid[i][j]] = 1
            square_visited[((i - 1) // 3) * 3 + ((j-1) // 3) + 1][grid[i][j]] = 1
print(*col_visited,sep='\n')
# ans = []
# def dfs(row,col):
#     if row==10:
#         temp = []
#         ans.append(grid)
#         for i in range(1,10):
#             for j in range(1,10):
#                 temp.append(grid[i][j])
#         ans.append(temp)
#         print(*temp,sep='\n')
#         print(len(temp),'--------')
#         return 0
#     elif col == 10:
#         dfs(row+1,1)
#         return 0
#     else:
#         if not square_visited[row][col] and not row_visited[row][col] and not col_visited[row][col]:
#             for i in range(1,10): #체크 안된 곳 모든 숫자 돌려보기
#                 square_visited[((row - 1) // 3) * 3 + ((col-1) // 3) + 1][i] = 1
#                 row_visited[row][i] = 1
#                 col_visited[col][i] = 1
#                 grid[row][col] = i
#                 dfs(row, col+1)
#                 grid[row][col] = 0
#                 square_visited[((row - 1) // 3) * 3 + ((col-1) // 3) + 1][i] = 0
#                 row_visited[row][i] = 0
#                 col_visited[col][i] = 0
#         else:
#             dfs(row, col + 1)
# dfs(1,1) # 1,1부터 시작
# print(*ans)