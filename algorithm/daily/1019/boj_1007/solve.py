"""
벡터매칭
평면상 N개의 점
모든 벡터는 위의 점 2개의 조합으로 나타난다.
벡터 매칭에 있는 벡터는 P의 개수의 절반, 벡터의 합의 길이의 최솟값 출력하기
"""
import sys
# sys.stdin = open('input.txt')

o = open('input.txt')
from math import sqrt
from itertools import combinations as cb
def vec(arr):
    global minv
    nx,ny = x,y
    for c,d in arr:
        nx -= 2*c
        ny -= 2*d
    minv = min(minv,sqrt(nx*nx + ny*ny))

ans = []
for t in range(int(next(o))):
    N = int(next(o))
    nums = []
    x=y=0
    for _ in range(N):
        a,b = map(int,next(o).split())
        x += a
        y += b
        nums.append([a,b])
    minv = int(1e9)
    for arr in cb(nums,N//2):
        vec(arr)
    ans.append(minv)
print(*ans,sep='\n')
# N개 전체를 순열로 돌리지 말고 처음부터 total을 구한뒤 n//2만 뺀다