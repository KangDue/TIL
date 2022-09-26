import sys
sys.stdin = open('input.txt')
"""
자연수 N을 몇번의 연산으로 M으로 만들자
연산은 +1, -1, *2, -10 의 연산이 있다.
최소의 연산 수는?
"""
from collections import deque
for t in range(int(input())):
    n,m = map(int,input().split())
    q = deque([n])
    visited = [0]*1000001
    visited[n] = 1
    while q:
        try:
            now = q.popleft()
            for nv in (now+1, now-1,now*2,now-10):
                if 1 <= nv <= 1000000 and not visited[nv]:
                    visited[nv] = visited[now] + 1
                    q.append(nv)
                    if nv == m:
                        raise Exception
        except:break
    print(f'#{t+1} {visited[m]-1}')