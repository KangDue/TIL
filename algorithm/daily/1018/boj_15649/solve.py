"""
N 과 M 1
"""
import sys,time
sys.stdin = open('input.txt')

# M 스위치 정보
from itertools import permutations as pm
n,m = map(int,input().split())
for i in pm(range(1,n+1),m):
    print(*i)