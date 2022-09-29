import sys
sys.stdin = open('input.txt')
"""
서강그라운드
예은이 낙하지점 중심으로 거리가 수색범위 이내 모든 아이템 습득 가능시
최대 아이템 개수는?
"""
import heapq
n,m,r = map(int,input().split())
area = [0]+[*map(int,input().split())]
graph = [[] for _ in range(n+1)]
INF = int(1e9)
for _ in range(r):
	x,y,z = map(int,input().split())
	graph[x].append([y,z])
	graph[y].append([x,z])
	maxv = 0
for i in range(1,n+1):
	q = [[0,i]]
	temp = 0
	dist = [INF] * (n+1)
	dist[i] = 0
	while q:
		d,now = heapq.heappop(q)
		if d > dist[now]:
			continue
		if d > m:
			break
		temp += area[now] #순서 잘 보자
		for nv,co in graph[now]:
			cost = d+co
			if cost < dist[nv]:
				dist[nv] = cost
				heapq.heappush(q,[cost,nv])
	maxv = max(maxv,temp)
print(maxv)