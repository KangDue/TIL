import sys
sys.stdin = open('input.txt')
"""
트리의 지름 구하기
최대값 구하기 = -로 변환후 최소값 구하기로 가야하는데
이때 방문처리 안하면 무한루프에 빠지니까 조심!
"""
# import heapq
# n = int(input())
# INF = int(1e9)
# tree = [[] for i in range(n+1)]
# for _ in range(n-1):
#     x,y,z = map(int,input().split())
#     tree[x].append([y,-z])
#     tree[y].append([x,-z])
# dist=[INF]*(n+1)
# dist[1] = 0
# q = [[0,1]]
# visited = [0]*(n+1)
# while q:
#     d,now = heapq.heappop(q)
#     visited[now] = 1
#     for nv,co in tree[now]:
#         cost = d + co
#         if dist[nv] > cost and not visited[nv]:
#             dist[nv] = cost
#             heapq.heappush(q,[cost,nv])
# next_idx = dist.index(min(dist))
#
# dist=[INF]*(n+1)
# dist[next_idx] = 0
# q = [[0,next_idx]]
# visited = [0]*(n+1)
# while q:
#     d,now = heapq.heappop(q)
#     visited[now] = 1
#     for nv,co in tree[now]:
#         cost = d + co
#         if dist[nv] > cost and not visited[nv]:
#             dist[nv] = cost
#             heapq.heappush(q,[cost,nv])
# print(-min(dist))


# 시간 가장빠른 코드
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    adj = [[] for _ in range(n+1)] # 트리 인접리스트
    ans = [(0,0)] * (n+1)
    for _ in range(n-1):
        p,c,w = map(int,input().rstrip().split())
        adj[p].append((c,w))
    for i in range(n,0,-1): # 트리의 leaf 노드 부터 탐색 시작
        mx,mx2 = 0,0
        for v,w in adj[i]: # 부모노드에 대해서
            t = w + ans[v][0] # 부모 노드와의 거리 w. ans[v][0]은 말단부터 v까지 거리

            if t > mx:
                mx2 = mx
                mx = t
            elif t > mx2:
                mx2 = t
            print(mx,mx2)
        ans[i] = (mx,mx2)
    ans.sort(reverse=True, key = lambda x: sum(x))
    print(sum(ans[0]))
if __name__ == '__main__':
    main()