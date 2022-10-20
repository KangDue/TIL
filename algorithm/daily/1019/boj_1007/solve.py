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
def vec(arr):
    global minv
    a=b=0
    for i in range(0,N,2):
        y1, x1 = arr[i]
        y2, x2 = arr[i+1]
        a += y2-y1
        b += x2-x1
    minv = min(minv, a*a + b*b)

from itertools import permutations as pm
ans = []
for t in range(int(next(o))):
    N = int(next(o))
    nums = [[*map(int,next(o).split())] for _ in range(N)]
    minv = int(1e9)
    for arr in pm(nums,N):
        vec(arr)
    ans.append(sqrt(minv))
print(*ans)

