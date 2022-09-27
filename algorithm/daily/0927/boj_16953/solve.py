import sys
sys.stdin = open('input.txt')
"""
A -> B
2를 곱하거나 1을 수 오른쪽에 추가
(한번 값이 B를 넘어가면 복귀 불가)
바꾸는데 필요한 연산의 최솟값에 1을 더한 값 출력
불가능하면 -1 출력
1<=A<=B<=1,000,000,000
queue하니까 메모리 초과 뜨네 ;
dfs로 해보자 이래도 메모리 초과뜨노;
원인은 visited 때문 visited를 B크기로 맞췄더니 초과
"""

# pypy에서 python으로 바꿧더니 dfs가 bfs 보다 빨라짐 ?? 왜이래
# DFS 버전 (재귀라 그런지 조오금 느림)
# A,B = map(int,input().split())
# visited = dict()
# INF = int(1e9)
# ans = INF
# def dfs(c=1,now=A):
#     global visited,ans
#     if now == B:
#         ans = min(ans,c)
#         return 0
#
#     for v in (now*2,now*10+1):
#         if v <= B and not visited.get(v):
#             visited[v] = 1
#             dfs(c+1, v)
#             visited.pop(v)
# dfs()
# if ans == INF:
#     print(-1)
# else:
#     print(ans)

#BFS 버전
from collections import deque
A,B = map(int,input().split())
visited = dict()
q = deque([[1,A]])
while q:
    try:
        c,now = q.popleft()
        for v in (now*2,now*10+1):
            if v > B: continue
            elif v == B:
                print(c+1)
                raise Exception
            elif not visited.get(v):
                visited[v] = 1
                q.append([c+1,v])
    except:
        break
else:
    print(-1)