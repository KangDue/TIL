import sys
sys.stdin = open('input.txt')
"""
트리의 지름 구하기
"""
import heapq
n = int(input())
INF = 1e9
tree = [[] for i in range(n+1)]
for _ in range(n-1):
    x,y,z = map(int,input().split())
    tree[x].append([y,z])
    tree[y].append([x,z])


