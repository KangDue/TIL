import sys
sys.stdin = open('input.txt')
"""
같은 조에 참여하고 싶은 사람 끼리 두 사람의 출석 번호를 종이에 적어 제출
한사람이 여러장 or 여러사람이 한자람 지목 모두 같은조가 된다.
1~N번까지 번호가 있을대 M장의 신청서가 제출, 몇개의 조가 있나?
#유니온 파인드 연습한거고, bfs로도 가능함.
bfs로는 했는데 유니온 파인드는 ㅠㅠ 3개맞 맞네 3/10 왜이럴까 ???
"""
# from collections import deque
# for t in range(int(input())):
#     n,m = map(int,input().split())
#     graph = [[] for _ in range(n+1)]
#     pairs = [*map(int,input().split())]
#     for i in range(0,2*m,2):
#         graph[pairs[i]].append(pairs[i+1])
#         graph[pairs[i+1]].append(pairs[i])
#     visited = [0] * (n+1)
#     c = 0
#     for i in range(1,n+1):
#         if not visited[i]:
#             c += 1
#             q = deque([i])
#             visited[i] = 1
#             while q:
#                 now = q.popleft()
#                 for nv in graph[now]:
#                     if not visited[nv]:
#                         visited[nv] = 1
#                         q.append(nv)
#     print(f'#{t+1} {c}')












def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    else:
        return x

def union(x,y):
    global parent
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
        for i in range(1,n+1): # 새로 추가
            if parent[i] == y:
                parent[i] = x
    else:
        parent[x] = y
        for i in range(1,n+1): #새로 추가
            if parent[i] == x:
                parent[i] = y

for t in range(int(input())):
    n,m = map(int,input().split())
    parent= [i for i in range(n+1)] #부모노드 테이블
    pairs = [*map(int,input().split())]
    for i in range(0,2*m,2):
        union(pairs[i], pairs[i+1])
    # for i in range(1,n+1): #뒤에서 합쳐질때 앞이 반영이 안됨.
    #     find(i)
    print(f'#{t+1} {len(set(parent[1:]))}')

"""
find 한번 안해주면 답 안나오는 반례
1
5 3
2 3 5 4 1 4
4 5를 그룹핑 하고 1 4를 그루핑하면 5가 버려짐.
이런일을 방지하려면 전체를 한 번 순회하며 find를 해주던가 ! 이게 맞음
rank정보를 저장하고 rank정보를 기반으로 합치거나 - 는 해도 소용 없음 이건 시간 복잡도 줄이는 전략
합쳐질때마다 부모를 자신으로 둔 자식 노드들을 전부 함께 업데이트 하던가 ! 이거도 맞음
"""