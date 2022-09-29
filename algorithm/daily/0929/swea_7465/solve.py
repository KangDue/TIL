import sys
sys.stdin = open('input.txt')
"""
창용 마을 무리의 개수
그루핑 문제?
union find or bfs

N명의 사람이 산다(1~N번)
서로 연결되면 하나의 무리로친다.
"""
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
        return parent[x]
    else:
        return x
def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
        for i in range(1,n+1):
            if parent[i] == y:
                parent[i] = x
    else:
        parent[x] = y
        for i in range(1,n+1):
            if parent[i] == x:
                parent[i] = y
for t in range(int(input())):
    n,m = map(int,input().split())
    parent=[i for i in range(n+1)]
    for _ in range(m): #마을 사람들 관계
        x,y = map(int,input().split())
        union(x,y)
    print(f'#{t+1} {len(set(parent[1:]))}')