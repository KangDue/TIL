import sys
sys.stdin = open('input.txt')
"""
N과 M
주어진 수열에서 중복되지않게 사전순으로 순열 생성
"""
from itertools import permutations as pm
n,m = map(int,input().split())
find = dict()
nums = sorted(map(int,input().split()))
for i in pm(nums,m):
    if not find.get(i):
        print(*i)
        find[i] = 1
