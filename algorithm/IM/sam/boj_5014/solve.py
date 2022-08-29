import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
스타트링크
:느낌상 숨바꼭질과 비슷
F =  총 건물의 층수 (1~1000000) 백만 닫힌구간
S = 현 위치
G = 골인지점
U = 위로가는 버튼
D = 아래로가는 버튼
갈수 있으면 몇번 엘베를 타야하나
없다면 'use the stairs' 출력
"""
if __name__ == "__main__":
    import sys
    r, sr = range, sys.stdin.readline
    from collections import deque,defaultdict
    F,S,G,U,D = map(int,sr().split())
    f = [0]*(F+1)
    visited = [0]*(F+1)
    q = deque([[S,0]])
    visited[S] = 1
    while q:
        v,step = q.popleft()
        if v == G:
            print(step)
            break
        for i in (v-D,v+U):
            if 1<= i <= F and visited[i]==0:#유효범위, 갈수 없는 층은 당연히 안감.
                q.append([i,step+1])
                visited[i] = 1
    else:
        print('use the stairs')


