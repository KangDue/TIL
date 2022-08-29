import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
몬스터잡기는 가면됨 (시간 x)
고객 확인도 가기만 하면됨 (시간 x)
초기위치 1,1 
몬스터1 고객1 각각 전부 확인시키는 최단시간을 구하시오
몬스터. 고객이 위치가 같은 경우는 없다.
몬스터와 고객의 위치는 1,1로 주어질 수 있다.
고객과 몬스터 1~4 (번호 같음) 몬스터는 양수, 고객은 음수
0은 아무것도 없는 경우,
"""
from collections import deque,defaultdict
for t in range(1,int(input())+1):
    n = int(input())#맵 nxn
    #딱히 좌표정보는 안중요하니까 걍 받자
    grid = [[*map(int,input().split())] for i in range(n)]
    visited = [[0 for i in range(n)] for j in range(n)]
    mc = []
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                mc.append([grid[i][j],i,j])
    graph = [[0 for i in range(len(mc)+1)] for j in range(len(mc)+1)]
    for i in range(len(mc)-1):
        for j in range(i+1,len(mc)):
            graph[mc[i][0]][mc[j][0]] = abs(mc[i][1]-mc[j][1])+abs(mc[i][2]-mc[j][2])
            graph[mc[j][0]][mc[i][0]] = abs(mc[i][1]-mc[j][1])+abs(mc[i][2]-mc[j][2])
    mcname = [i[0] for i in mc]
    def permu(x,n):
        for i in range(len(x)):
            if n == 1:
                yield [x[i]]
            else:
                for e in permu(x[:i]+x[i+1:],n-1):
                    yield [x[i]]+e
    def check(x):
        for i in range(1,len(mc)//2+1):#몬스터 넘버
            if x.index(i) > x.index(-i): #고객보다 몬스터가 뒤에있다? 끝
                return 0
        else:
            return 1
    minv = 1000000
    for i in permu(mcname,len(mcname)): #가능한 모든 조합중.
        ans = 0
        if check(i): #가능한 경우의 수만
            for k in mc:
                if k[0] == i[0]:
                    ans += k[1]+k[2] #헌터에서 몬스터까지 초기거리
            for j in range(len(i)-1):#각 노드간 거리
                ans += graph[i[j]][i[j+1]]
            #경로상 거리와 minv값 비교
            if minv > ans: minv = ans
    print(minv)

