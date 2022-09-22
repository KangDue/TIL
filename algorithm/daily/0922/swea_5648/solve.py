import sys
sys.stdin = open('input.txt')
"""
원자소멸 시뮬레이션
원자 최초위치 x,y 좌표로 주어짐
상하좌우로 움직임. 1초에 1씩 이동
최초 위치에서 동시에 이동을 시작한다.
두개이상 부딪히면 원자들은 에너지 방출하고 소멸
원자들이 소멸하며 방출하는 에너지의 총합
웬만하면 실수형은 쓰지 말자! (메모리를 더 잡아먹고, 처리하는데 시간이 int보다 오래걸림)
"""

#x,y, 이동방향, 보유 에너지
#초기위치 -1000 ~ 1000
#방문처리 필요없음, 그저 가기만 하면됨
from collections import deque,defaultdict
to = [[0,1],[0,-1],[-1,0],[1,0]]#상하좌우 = 0 1 p2 3 x,y 좌표계 기준
for t in range(int(input())):
    n = int(input())
    graph = defaultdict(list)
    # q = deque([])
    # atoms = []
    for _ in range(n):
        x,y,d,k = map(int,input().split())
        graph[(2*x,2*y)].append([d,k])
        # q.append([x,y,d,k,0])
    ans = 0
    for _ in range(4001):
        gl = list(graph.keys())
        for i in gl:
            if len(graph[i]) > 1:
                ans += sum(map(lambda x: x[1], graph[i]))
                graph.pop(i)
            else: #1개만 있던거라 삭제해도 무방
                x,y = i
                d,k = graph[i][0]
                # if -1000<=x+to[d][0]<=1000 and -1000<=y+to[d][1]<=1000:
                graph[(x+to[d][0], y+to[d][1])].append([d,k])
                graph.pop(i)
    print(f'#{t + 1} {ans}')

    # gs = 0
    # addon = 0
    # while q:
    #     x,y,d,k,step = q.popleft()
    #     if step != gs:
    #         gs+=1
    #         if len(graph[(x,y)]) > 1:
    #             addon += sum(map(lambda x:x[1],graph[(x,y)]))
    #             graph.pop((x, y))
    #             continue
    #     if [d,k] in graph[(x,y)]:
    #         nx = x+to[d][0]
    #         ny = y+to[d][1]
    #         if -1000 <= ny <= 1000 and -1000 <= nx <= 1000:
    #             q.append([nx,ny,d,k,step+1])
    #             graph[(x,y)].remove([d,k])
    #             graph[(nx,ny)].append([d,k])
    # print(f'#{t+1} {addon}')


