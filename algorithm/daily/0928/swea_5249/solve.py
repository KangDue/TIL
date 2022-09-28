import sys
sys.stdin = open('input.txt')
"""
MST
0번부터 v번까지의 노드
E개의 간선
여기서 최소신장트리 구하기
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

    if x<y:
        parent[y] = x
        for i in range(v):
            if parent[i] == y:
                parent[i] = x
    else:
        parent[x] = y
        for i in range(v):
            if parent[i] == x:
                parent[i] = y

for t in range(int(input())):
    v,e = map(int,input().split())
    parent = [i for i in range(v+1)]
    edges = []
    for _ in range(e):
        edges.append([*map(int,input().split())])
    edges.sort(key=lambda x:(x[2],x[1]),reverse = True)
    mst = []
    mst_v = 0
    i=0                   #점이 v+1개임
    while len(mst) < v: #mst 의 길이가 v이 될 때 까지 간선 추가
        x,y,val = edges.pop() #가중치 큰거부터 뽑기
        if parent[x] != parent[y]:
            union(x,y)
            mst.append([x,y])
            mst_v += val
    print(f'#{t+1} {mst_v}')


