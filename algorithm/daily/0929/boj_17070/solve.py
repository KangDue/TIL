import sys
sys.stdin = open('input.txt')
"""
파이프 옮기기
NxN 새집에서 행열번호는 1부터 시작
파이프는 길이가 2이며 오른쪽으로,아래로,대각선(좌상우하)으로 걸칠 수 있다.
밀면서 45도만 회전 가능 , 즉 수평,수직에선 2방향, 대각선에선 3방향 가능
처음 파이트는 1,1과 1,2를 차지하는 중
파이프의 한쪽 끝을 N,N으로 이동 시키는 방법의 수
벽은 1로 표시되어있고 여기로 못간다.
무조건 골을 향해 나아가니 visited 필요 x (DAG)
굳이 이렇게 좌표 이동이 아니라 숫자 덧셈해도 빠를듯
#파이프는 빈칸만 차지해야한다. 걸치는 영역 전부 고려
70% 시간초과.
87% 시간초과
"""

import sys
#dfs 풀이
# to = [[1,0],[0,1],[1,1]]#상태 0,1,2로 구분 (아래,오른쪽, 대각선)
# n = int(sys.stdin.readline())
# grid = [['0']*(n+1)] + [['0']+[*sys.stdin.readline().split()]+['0'] for _ in range(n)] + [['0']*(n+1)]
# tot = 0
# def check(r=1,c=2,direct=1):#초기위치
# 	global tot
# 	for i in range(3):
# 		if not direct and i==1: continue
# 		if direct == 1 and not i: continue
# 		if i == 2 and (grid[r+1][c]=='1' or grid[r][c+1]=='1'): continue
# 		ny = r + to[i][0];nx = c + to[i][1]
# 		if ny <= n and nx <= n and grid[ny][nx]=='0': # 일단 적어도 가는곳은 벽이면 안됨.
# 			if ny == n and nx == n:
# 				tot+=1
# 				return 0
# 			else:
# 				check(ny,nx,i)
# check()
# print(tot)


#dp 풀이
import sys
n = int(sys.stdin.readline())
grid = [[*sys.stdin.readline().split()] for _ in range(n)]
dp  = [[[0]*3 for _ in range(n)] for _ in range(n)]
dp[0][1][1] = 1
for i in range(n):
	for j in range(2,n):
		if grid[i][j] == '1': continue
		if (1<=i and grid[i-1][j] =='1') or (grid[i][j-1] == '1'):
			dp[i][j][0] = dp[i - 1][j][0] + dp[i - 1][j][2]
			dp[i][j][1] = dp[i][j - 1][1] + dp[i][j - 1][2]
		else:
			dp[i][j][0] = dp[i - 1][j][0] + dp[i - 1][j][2]
			dp[i][j][1] = dp[i][j - 1][1] + dp[i][j - 1][2]
			dp[i][j][2] = sum(dp[i-1][j-1])
# print(*dp,sep='\n')
print(sum(dp[n-1][n-1]))