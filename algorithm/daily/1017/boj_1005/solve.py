"""
ACM craft

#그래프 이상하게 주면 어쩌지 했는데 모든 그래프 연결 상태로만 주네
- 건설순서는 모든 건물이 건설 가능하도록 주어진다.

위상정렬을 해봅시다 !!^^
1차시도 58% 틀림
2차시도 58% 틀림
... 질문 게시판 보니 네트웤이 여러개인 경우도 있을 수 있다함.
"""
import sys
# sys.stdin = open('input.txt')

o = open('input.txt')
from collections import deque
for i in range(int(next(o))):
    n,k = map(int,next(o).split())
    weight = [0] + [*map(int,next(o).split())]
    degree = {i:0 for i in range(1,n+1)}
    graph = [[] for _ in range(n+1)]
    for _ in range(k): #그래프를 역으로 들어가 보자
        x,y = map(int,next(o).split())
        graph[x].append(y)
        degree[y]+=1
    target = int(next(o))

    q = deque()
    time = [0]*(n+1)
    for i in range(1,n+1):
        if not degree[i]:
            q.append(i)

    while q:
        try:
            now = q.popleft()
            for nv in graph[now]:
                degree[nv] -= 1
                time[nv] = max(time[nv],time[now] + weight[now])
                if not degree[nv]:
                    q.append(nv)
                    degree.pop(nv)
                    if nv == target:
                        raise Exception
        except:
            break
    time[target] += weight[target]
    print(time[target])

# 내 추측으론 가지가 갈라지면서 target과는 필수적인 요소는 아닌데
# 시간 max의 최대값으로 넣어버려서 이런 문제가 생긴듯 하다.
# 그래프 부모찾기부터 해주자! 가 잘 안되누 ...
