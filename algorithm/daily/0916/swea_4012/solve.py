import sys
sys.stdin = open('input.txt')
"""
두명의 손님에게 음식을 제공하려고 한다.
N개의 식재료가 있다. 각각 N/p2 개씩 나누오 두개의 요리를 한다.(짝수)
비슷한 맛의 음식을 만드려면 맛의 차이가 최소가 되야한다.
주어지는 grid는 각 요리들간의 시너지 값이다.
음식 = 시너지들의 합
경우의수 갈기면됨.
음식간 맛의 차이가 최소화되는 값을 찾고 출력
"""
def make(arr):
    ans = 0
    l = len(arr)
    for i in range(l-1):
        for j in range(i+1,l):
            ans += grid[arr[i]][arr[j]]
            ans += grid[arr[j]][arr[i]]
    return ans

from itertools import combinations as cb
for t in range(int(input())):
    n = int(input())
    grid = [[*map(int,input().split())] for _ in range(n)]
    ing = set(range(n))
    minv = 20000*16+1
    for i in cb(range(n),n//2):
        temp = [*ing.difference(i)]
        minv = min(minv, abs(make(i)-make(temp)))
    print(f'#{t+1} {minv}')