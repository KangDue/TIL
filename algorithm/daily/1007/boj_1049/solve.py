"""
기타줄
개당 가격이든, 패키지 가격이든 둘중 하나라도 가장 낮은거부터 나열하면 된다.
묶음중 제일 싼거랑
개당중 제일 싼거를 구분해야함
그래야 6개 나눈 나머지에 대해 처리 가능.
"""

import sys
sys.stdin = open('input.txt')
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
minp = mine = int(1e9)
for _ in range(m):
    p,e = map(int,input().split())
    minp = min(minp,p)
    mine = min(mine,e)
a,b=divmod(n,6)
if 6*mine <= minp:
    print(n*mine) #개당이 패키지보다 싸면 그냥 개당으로 다 사면 됨
elif b: # 나머지가 있을 때
    if minp >= b*mine: #패키지가 싸긴한데 나머지를 개당처리하는거 보다 패키지가 더 쌀때
        print(minp*a + mine*b)
    else:
        print(minp*(a+1))
else: #나머지 없을때
    print(a*minp)