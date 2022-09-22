import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
숨바꼭질2
수빈이는 현위치 0~100,000 (닫힌구간)
자기 위치에서 x-1, x+1 또는 p2*x로 1초뒤에 이동한다.
시작점 n, 도착점 k
가장빠른 방법은 몇초만에 찾는가?
그리고 몇가지인가?
비트연산자는 정말 1,0 스위칭 할때만 쓰자 ... ㅠ
"""
if __name__ == "__main__":
    import sys
    from collections import deque,defaultdict
    r,sr=range,sys.stdin.readline
    n,k=map(int,sr().split())
    q=deque([[n,0]])
    visited = [0]*100001
    dist = []
    while q:
        v,time = q.popleft()
        visited[v] = 1 #여기서 체크하면 중복인곳을 재방문 한다.(경우의 수 체크가능)
        if v==k:
            dist.append(time)
        for i in (2*v,v+1,v-1):
            if 0<= i <= 100000: #~는 not 비트 부호 자체를 뒤집어 버린다..
                if visited[i]==0: #여기서 방문했다고 체크하면 중복인값을 방문하지 않는다.
                    # 1-3, p2-3, 4-3 이면 3으로 가는 3가지 경우가 있으나 여기서 중복체크를 처음부터하면 1개만 간다.
                    q.append([i,time+1])
    print(dist[0],dist.count(dist[0]))