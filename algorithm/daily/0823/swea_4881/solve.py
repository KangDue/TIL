import sys
sys.stdin = open('input.txt')

from itertools import permutations as pm
for t in range(int(input())):
    n = int(input())
    nums = [list(map(int,input().split())) for i in range(n)]
    minv = 10*n+1
    for i in pm(range(n), n):
        temp = 0
        for z in range(n):
            temp += nums[z][i[z]]
            if temp >= minv:
                break
        if minv > temp:
            minv = temp
    print(f'#{t+1} {minv}')