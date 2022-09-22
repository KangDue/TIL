import sys
"""
최소비용구하기
- 한 지점으로의 최단 거리만 구할꺼면 아래와 같이 빠르게 종료를 해주어야함.
안그러면 시간초과
시간 1위를 보면(파이썬) heapq를 쓰지않고 단순 list에서 min값 indexing 으로 풀었음.
작은 숫자 - 많은 case 면 이런 linear한게 빠르기도 함.
"""
o = open('input.txt')
import heapq
n = int(next(o))
m = int(next(o))
graph = [[] for i in range(n+1)]
for _ in range(m): #단방향 그래프 인듯?
    x,y,w = map(int,next(o).split())
    graph[x].append([y,w])
start,end = map(int,next(o).split())
dist = [1e9]*(n+1)
dist[start] = 0
# q = [[0,start]]
# dist[1]=0
# while q:
#     d,now = heapq.heappop(q)
#     if now == end:
#         print(dist[now])
#         break
#     for nv,co in graph[now]:
#         cost = d + co
#         if cost < dist[nv]:
#             dist[nv] = cost
#             heapq.heappush(q,[cost,nv])

#그러면 직접한번 리니어하게 구현해보자!
nodes = list(range(1,n+1))
visited = [0]*(n+1)
for i in range(m-1):
    now = min(nodes,key = lambda x:(visited[x],x))
    visited[now] = 1
    for nv,co in graph[now]:
        cost = dist[now] + co
        if cost < dist[nv]:
            dist[nv] = cost
print(dist[end])







#참고코드
# import sys
#
# input = sys.stdin.readline
# INF = 987654321
#
# v = int(input())
# e = int(input())
#
# graph = [[] for _ in range(v + 1)]
# for _ in range(e):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#
# start, end = map(int, input().split())
#
# visited = [False for _ in range(v + 1)]
# distance = [INF for _ in range(v + 1)]
#
#
# def getSmallestIndex():
#     minValue = INF
#     index = 0
#     for i in range(1, v + 1):
#         if not visited[i] and minValue > distance[i]:
#             minValue = distance[i]
#             index = i
#     return index
#
#
# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True
#     for i in graph[start]:
#         if distance[i[0]] > i[1]:
#             distance[i[0]] = i[1]
#     for _ in range(v - 1):
#         now = getSmallestIndex()
#         visited[now] = True
#         for next in graph[now]:
#             cost = distance[now] + next[1]
#             if distance[next[0]] > cost:
#                 distance[next[0]] = cost
#
#
# dijkstra(start)
# print(distance[end])