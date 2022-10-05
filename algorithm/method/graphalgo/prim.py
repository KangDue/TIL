INF = int(1e9)
N = 7
G = [[[1,32],[2,31],[5,60],[6,51]],
     [[0,31],[2,21]],
     [[0,31],[1,21],[4,46],[6,25]],
     [[4,34],[5,18]],
     [[3,34],[5,40],[6,51]],
     [[0,60],[3,18],[4,40]],
     [[0,51],[4,51]]]

#선형 탐색,
def prim(G,start):
    value = [INF] * N
    pair = [None] * N
    visited = [0] * N
    value[start] = 0

    for _ in range(N):
        mindex = -1
        minv = INF
        for i in range(N):
            if not visited[i] and value[i] < minv:
                mindex = i
                minv = value[i]

        visited[mindex] = 1

        for nv,cost in G[mindex]:
            if not visited[nv] and cost < value[nv]:
                value[nv] = cost
                pair[nv] = mindex
    print(pair)
    print(value)

prim(G,0)
import heapq
def hprim(G,start):
    global N
    weights = [INF] * N
    pairs = [None] * N
    visited = [0] * N
    weights[start] = 0
    q = [[0,start]]
    while N > 1:
        value, min_node = heapq.heappop(q)
        if not visited[min_node]:
            visited[min_node] = 1
            N -= 1
            for nv,cost in G[min_node]:
                if not visited[nv] and cost < weights[nv]:
                    weights[nv] = cost
                    pairs[nv] = min_node
                    heapq.heappush(q,(cost,nv))
    print(pairs)
    print(weights)
hprim(G,0)

#---------------------------------------------------------------
nG = [
    [0,1,32],
    [0,2,31],
    [0,5,60],
    [0,6,51],
    [1,2,21],
    [2,6,25],
    [2,4,46],
    [3,4,34],
    [3,5,18],
    [4,5,40],
    [4,6,51]
]

def find(x):
    global parent
    if x != parent[x]:
        parent[x] = find(parent[x])
        return parent[x]
    else:
        return x

def union(x,y):
    global parent
    x = find(x)
    y = find(y)
    if x<y:
        parent[y] = x
    else:
        parent[x] = y

parent = [i for i in range(N)]

def kruskal(G):
    mst = []
    G.sort(key = lambda x:(x[2],x[1]),reverse = True)
    mst_cost = 0
    while len(mst) < N-1: #N-1개 되면 종료
        u,v,val = G.pop()
        if find(u) != find(v):
            union(u,v)
            mst.append((u,v))
            mst_cost += val
    print(mst_cost)
kruskal(nG)









































