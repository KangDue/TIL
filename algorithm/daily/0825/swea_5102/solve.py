# 미로 탈출 가능 불가능 ?
# 1은 벽, 2는 출발, 3은 도착, 0은 길
import sys
sys.stdin = open('input.txt')


# def bfs(now,c): 모든경로 탐색.
#     global graph,visited,count
#     if now == g:
#         count = c
#     else:
#         for i in graph[now]:
#             if visited[i] == 0:
#                 visited[i]=1
#                 bfs(i,c+1)
#                 visited[i]=0

from collections import deque
d,w,r=int,input,range
for t in r(d(w())):
    v,e = map(d,w().split())
    graph = [[] for i in r(v+1)]
    visited = [0 for i in r(v+1)]
    for i in r(e):
        a,b = map(d,w().split())
        graph[a].append(b) ; graph[b].append(a)
    s,g = map(d,w().split())#출발 도착
    q = deque([(s,0)])
    visited[s]=1
    ans = 0
    while len(q):
        try:
            now = q.popleft()
            for i in graph[now[0]]:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append((i,now[1]+1))
                    if i == g:
                        ans = now[1]+1
                        raise ValueError #모든 경로 다 찾지 말고 조기종료 해야함.
        except:
            break
    print(f'#{t + 1} {ans}')































# def mat_mul(x,y):
#     le = len(x)
#     temp1 = [[0 for i in range(le)] for k in range(le)]
#     temp2 = list(zip(*y))
#     for i in range(le):
#         for k in range(le):
#             temp1[i][k] = list_mul(x[i],temp2[k])
#     return temp1
#
# def list_mul(x,y):
#     ans = 0
#     le = len(x)
#     for i in range(le):
#         if not(any(x)) or not(any(y)):
#             return 0
#         ans += x[i]*y[i]
#     return ans
#
# T = int(input())
# for t in range(1,T+1):
#     v,e = map(int,input().split())#정점과 간선 수
#     mat = [[0 for i in range(v+1)] for i in range(v+1)] #인접행렬생성
#     for i in range(e): #그래프 생성
#         a,b = map(int,input().split())
#         mat[a][b] = 1
#         mat[b][a] = 1
#     start,goal = map(int,input().split()) #출발,목표 노드
#     noway =False
#     if mat[start][goal] == 1:
#         count = 1
#     else:
#         count = p2
#         temp = mat_mul(mat,mat)
#         while 1: #최대 길이가 점의 갯수임. (순환x)
#             if temp[start][goal] > 0 :
#                 break
#             elif count > v :
#                 noway = True
#                 break
#             else:
#                 temp = mat_mul(temp,mat) #점점 곱해나간다
#                 count += 1
#     if noway:
#         print(f'#{t} 0')
#     else:
#         print(f'#{t} {count}')