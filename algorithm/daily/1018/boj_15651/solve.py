"""
N 과 M 1
"""
import sys,time
sys.stdin = open('input.txt')

# M 스위치 정보
from itertools import product
n,m = map(int,input().split())
for i in product(range(1,n+1),repeat=m):
    print(*i)