import sys
# sys.stdin = open('input.txt')
"""
최소비용 구하기 2
(유향그래프)
1000개의 도시, 100000개의 버스 (max)
A에서 B도시까지 최소 비용과 그 노선
path 를 기억하는 방법으로 path 리스트를 직접 추가 할 수도 있지만
visited로 부모노드를 기억하게 하는것도 한 가지 방법
"""
from heapq import heappop as hpop
from heapq import heappush as push
# class link:
#     def __init__(self,node,weight=None,parent=None):
#         self.parent=parent
#         self.node = node
#         self.weight = weight
#     def __str__(self):
#         return str([self.node,self.weight])
#     def __repr__(self):
#         return str([self.node,self.weight])
#     def __gt__(self, other):
#         return self.value > other.value
#     def __lt__(self, other):
#         return self.value < other.value
# from heapq import heappop as hpop
# from heapq import heappush as push
# o = open('input.txt')
# n = int(next(o))
# m = int(next(o))
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     x,y,z = map(int,next(o).split())
#     graph[x].append((y,z))
# start,goal = map(int,next(o).split())
# INF = int(1e10)
# dist = [INF]*(n+1)
# dist[start] = 0
# q = [[0,start,[start]]]
# while q:
#     d,now,path = hpop(q)
#     if d > dist[now]:
#         continue
#     if now == goal:
#         break
#     for nv,co in graph[now]:
#         cost = d + co
#         if cost < dist[nv]:
#             dist[nv] = cost
#             push(q,[cost,nv,path+[nv]])
# print(d)
# print(len(path))
# print(*path)


from heapq import heappop as hpop
from heapq import heappush as push
o = open('input.txt')
n = int(next(o))
m = int(next(o))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y,z = map(int,next(o).split())
    graph[x].append((y,z))
start,goal = map(int,next(o).split())
INF = int(1e10)
dist = [INF]*(n+1)
dist[start] = 0
parent = [0] * (n+1)
q = [[0,start]]
while q:
    d,now = hpop(q)
    if d > dist[now]:
        continue
    if now == goal:
        break
    for nv,co in graph[now]:
        cost = d + co
        if cost < dist[nv]:
            dist[nv] = cost
            parent[nv] = now
            push(q,[cost,nv])
print(d)
path =[]
while goal:
    path.append(goal)
    goal = parent[goal]
path.reverse()
print(len(path))
print(*path)




