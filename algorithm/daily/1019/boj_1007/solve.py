"""
벡터매칭
평면상 N개의 점
모든 벡터는 위의 점 2개의 조합으로 나타난다.
벡터 매칭에 있는 벡터는 P의 개수의 절반, 벡터의 합의 길이의 최솟값 출력하기
"""
import sys
# sys.stdin = open('input.txt')

o = open('input.txt')
from itertools import combinations as cb
from math import sqrt
def vec(p1,p2):
    return p2[0]-p1[0],p2[1]-p1[0]

for t in range(int(next(o))):
    N = int(next(o))
    nums = [[*map(int,next(o).split())] for _ in range(N)]
    minv = int(1e9)
    visited = [0]*N
    #한 벡터에서 시작해서 다른 벡터로 끝나는 벡터 들의 집합!
    def dfs(count = 0, a=0, b=0, before=[]):
        global minv,N,visited
        if count == N:
            minv = min(minv,sqrt(a*a+b*b))
            return 0
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                if count%2:#홀수
                    c,d = vec(before,nums[i])
                    dfs(count + 1,a + c, b + d)
                else:
                    dfs(count + 1, a, b, nums[i])
                visited[i] = 0

    dfs()
    print(minv)