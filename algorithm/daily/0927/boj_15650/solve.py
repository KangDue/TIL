import sys
sys.stdin = open('input.txt')
"""
N과 M
자연수 1~M까지 아래 조건 만족하는 길이 M 수열
1부터 N 까지 중복없이 M개, 오름차순
"""
from itertools import combinations as cb
n,m = map(int,input().split())
for i in cb(range(1,n+1),m):
    print(*i)


# 다른 숏코드 참고
def backTracking(idx, string):
    visited[idx] = 1
    if visited.count(1) == M:
        print(string)
        visited[idx] = 0
        return
    for j in range(idx+1, len(mylist)):
        if visited[j] == 0:
            backTracking(j, string+' '+str(mylist[j]))
    visited[idx] = 0

N, M = map(int, input().split())

mylist = list(range(1, N+1))
visited = [0]*len(mylist)

for i in range(len(mylist)):
    backTracking(i, str(mylist[i]))