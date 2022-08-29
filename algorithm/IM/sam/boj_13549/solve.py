import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
숨바꼭질3
heapq써버리면 순간이동만한다.
"""
if __name__ == "__main__":
    import sys
    r, sr = range, sys.stdin.readline
    from collections import deque,defaultdict
    n,k = map(int,sr().split())
    nums = [0]*100001
    visited = [0]*100001
    q = deque([[0,n]])
    dist=defaultdict(int)
    while q:
        time,v = q.popleft()
        visited[v] = 1
        if v==k:#최단거리 출력#break 때려버리면 최단거리가 아님.
            dist[time]+=1
        tp = 2 * v#순간이동할 떄
        if 0<= tp <= 100000 and visited[tp] == 0:
            q.append([time,tp])
        for i in (v+1,v-1):#한 칸 갈때
            if 0<= i <= 100000 and visited[i] == 0:
                q.append([time+1,i])
    a = list(dist.items())
    a.sort(key=lambda x:x[0])#시간 짧은순 정렬
    print(a[0][0])








