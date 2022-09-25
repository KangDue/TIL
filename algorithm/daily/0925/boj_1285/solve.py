import sys
sys.stdin = open('input.txt')
"""
동전 뒤집기
NxN 동전 앞뒤로 중 하나인 상태로 놓임.
임의의 한행 또는 한열 전부 뒤집기 가능.
뒷면이 위를 향하는 동전의 개수 최소화!
"""
from itertools import combinations as cb
rev = {'H':'T','T':'H'}
def cr(r):
    global coins
    for i in range(n):
        coins[r][i] = rev[coins[r][i]]

def ccount(c):
    global coins
    h=t=0
    for i in range(n):
        if coins[i][c] == 'H': h+=1
        else: t += 1
    return h,t

def check(r=0):
    global ans
    if r==n:
        temp = 0
        for c in range(n):
            h,t = ccount(c)
            if h > t: temp += t
            else: temp += h
        ans = min(ans,temp)
        return 0
    check(r + 1) #재귀 적으로 행 뒤집는 모든 case 생성
    cr(r)
    check(r + 1) #이후 열 교체는 H가 많은것만 뒤집음

n = int(input())
coins = [[*input()] for _ in range(n)]
ans = n*n
check()
print(ans)