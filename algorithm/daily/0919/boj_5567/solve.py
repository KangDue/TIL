import sys
sys.stdin = open('input.txt')
"""
결혼식
동기는 모두 N명이고 이들의 학번은 1~N (상근이가 1번)
자기 친구와 친구의 친구까지만 초대
"""
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
tree = [[] for i in range(n+1)]
visited = [0] * (n+1)
visited[1]=1
for _ in range(int(input())):
    x,y = map(int,input().split())
    tree[x].append(y)
    tree[y].append(x)

c=dict() # dfs 왜 안대나 했더니 거리 1인걸 고려 안함 ㅋ;
def dsol(v,d=0):
    global c
    c[v]=1
    if d == 2: return 0
    for i in tree[v]:
        if not visited[i]:
            visited[i]=1
            dsol(i,d+1)
            visited[i]=0
dsol(1)
print(sum(c.values())-1)


#bfs 풀이
# q=deque([[1,0]])
# visited = [0] * (n+1)
# visited[1]=1
# for _ in range(int(input())):
#     x,y = map(int,input().split())
#     tree[x].append(y)
#     tree[y].append(x)
# while q:
#     v,d = q.popleft()
#     if d == p2:break
#     for i in tree[v]:
#         if not visited[i]:
#             q.append([i,d+1])
#             visited[i]=1
# print(sum(visited)-1)