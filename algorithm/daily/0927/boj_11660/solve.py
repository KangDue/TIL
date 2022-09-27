import sys
# sys.stdin = open('input.txt')
"""
구간합 구하기
NxN 행렬에서 주어진 구간 x1,y1 ~ x2,y2 를 좌상단, 우하단 끝점으로 하는 사각형에
둘러싸인 구간의 합 구하기
x1 <= x2, y1<= y2
시간초과뜨네... input 문제도 아닌듯.
출력을 한꺼번에 해보자. M이 최대 10만개라 먹힐지도 ? 안먹히네
#dp가 답이다!
#누적합으로 행렬 미리 갱신하고 r2c2에서 r1c1 뺴면 될듯
"""
# dp 새로 안만들고 grid만 조작했는데 오히려 느려짐... ??? 뭐지
o = open('input.txt')
n,m = map(int,next(o).split())
grid =[[0]*(n+1)] + [[*map(int,('0 '+next(o)).split())] for _ in range(n)]
ans = [0]*m
for i in range(1,n+1):
    for j in range(1,n+1):
        grid[i][j] += grid[i-1][j] + grid[i][j-1] - grid[i-1][j-1]
for i in range(m):
    r1,c1,r2,c2 = map(int,next(o).split())
    ans[i] = grid[r2][c2] + grid[r1-1][c1-1] - grid[r1-1][c2] - grid[r2][c1-1]
print(*ans,sep='\n')




# dp try 1 : 맞긴한데 줄여보자!
# dp = [[0]*(n+1) for _ in range(n+1)]
# for i in range(1,n+1): #첫 가로
#     dp[1][i] = dp[1][i-1] + grid[1][i]
# for j in range(1,n+1): # 첫 세로
#     dp[j][1] = dp[j-1][1] + grid[j][1]
# for i in range(2,n+1): # 내부
#     for j in range(2,n+1):
#         dp[i][j] = dp[i-1][j] + dp[i][j-1] + grid[i][j] - dp[i-1][j-1]
# print(*dp,sep='\n')
# print(*grid,sep='\n')