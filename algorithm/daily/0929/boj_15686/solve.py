import sys
sys.stdin = open('input.txt')
"""
치킨배달
NxN 크기 도시 각칸은 빈칸 0 ,치킨집 2,집 1 중 하나다.
좌표 r,c(row,col)은 1,1부터 시작.
치킨거리 = 집과 가장 가까운 치킨집 사이의 거리.
도시의 치킨 거리는 모든 치킨 거리의 합
거리는 맨해튼 거리.
치킨집을 최대 M개만 살리고, 나머지 모두 폐업시켜야 한다.
어떻게 고르면 도시의 치킨 거리가 minimum이 될까?
치킨집 개수는 M보다 크거나 같고 13보다 이하이다.

# bfs 조지니까 바로 시간초과 뜨네 ㅋㅋㅋ; 잘보니 그냥
조합문제인갑네
한개씩 더해서 가지치기도 가능한거 같은데 귀찮으니 pass
역시나 맞은거 보니 dfs 가지치기 (백트래킹 문제)
"""
def md(x,y):
	return abs(x[0]-y[0]) + abs(x[1]-y[1])
from itertools import combinations as cb
n,m = map(int,input().split())
grid = [[0]*(n+1)]+[[0]+[*map(int,input().split())] for _ in range(n)]
chick = []
house = dict()
for i in range(1,n+1):
	for j in range(1,n+1):
		if grid[i][j] == 2:
			chick.append([i,j])
		elif grid[i][j]:
			house[(i,j)] = 0
#각 치킨집 별 출발, 최소값 업데이트
minv = int(1e9)
for i in range(m):
	for choice in cb(chick,i+1): #choice
		temp = {k: 0 for k in house}
		for r,c in choice:
			for each in temp:
				if temp[each]:
					temp[each] = min(temp[each],md((r,c),each))
				else:
					temp[each] = md((r,c),each)
		minv = min(minv,sum(temp.values()))
print(minv)







"""
-----------------------------------
"""
# to = [[1,0],[-1,0],[0,1],[0,-1]]
# from collections import deque
# from itertools import combinations as cb
# n,m = map(int,input().split())
# grid = [[0]*(n+1)]+[[0]+[*map(int,input().split())] for _ in range(n)]
# chick = []
# house = 0
# for i in range(1,n+1):
# 	for j in range(1,n+1):
# 		if grid[i][j] == 2:
# 			chick.append([i,j])
# 		elif grid[i][j]:
# 			house += 1
#각 치킨집 별 출발, 최소값 업데이트

# bfs접근
# minv = int(1e9)
# for i in range(m):
# 	for choice in cb(chick,i+1):
# 		price = [[0] * (n + 1) for _ in range(n + 1)]
# 		for r,c in choice:
# 			hc = 0
# 			visited = [[0]*(n+1) for _ in range(n+1)]
# 			q = deque([[0,r,c]])
# 			visited[r][c] = 1
# 			while q:
# 					d,y,x = q.popleft()
# 					if grid[y][x] == 1:
# 						hc += 1
# 					if hc == house:
# 						break
# 					for dy,dx in to:
# 						ny = y+dy; nx = x+dx
# 						if 1<=ny<=n and 1<=nx<=n and not visited[ny][nx]:
# 							if grid[ny][nx] == 1 and price[ny][nx]: #집 방문시, 이미 업뎃 됬다면
# 								price[ny][nx] = min(price[ny][nx],d+1)
# 							elif grid[ny][nx] == 1 and not price[ny][nx]: #집 방문시, 업뎃 전
# 								price[ny][nx] = d + 1
# 							visited[ny][nx] = 1
# 							q.append([d+1,ny,nx])
# 		# print(*price,sep='\n')
# 		# print("------------")
# 		minv = min(minv, sum(sum(price,[])))
# print(minv)
