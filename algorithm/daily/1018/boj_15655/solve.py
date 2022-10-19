"""
N 과 M 1
"""
import sys,time
sys.stdin = open('input.txt')

# M 스위치 정보
from itertools import combinations as cb
n,m = map(int,input().split())
nums = sorted(map(int,input().split()))
for i in cb(nums,m):
    print(*i)