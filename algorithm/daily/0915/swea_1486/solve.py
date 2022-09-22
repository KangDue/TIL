import sys
sys.stdin = open('input.txt')
"""
높이가 B인 선반이 하나 있다.
N명의 점원이 있다. 점원의 키는 H로 탑을 쌓아 선반위의 물건을 쓸 수 있다.
1명이상 탑을 쌓는다.
높이가 B이상인 탑중에서 높이가 가장 낮은 탑을 찾자.
<답>
#1 1
#p2 4
#3 27
#4 11
#5 42
#6 32
#7 p2
#8 3
#9 25
#10 0
"""

#그냥 보면 단순 조합문제
from itertools import combinations as cb
for t in range(int(input())):
    n,b = map(int,input().split())
    s = [*map(int,input().split())]
    s.sort()
    maxv = 10000*20+1
    for j in range(n+1):
        for i in cb(s,j):
            a = sum(i)
            if a>=b and a<=maxv: maxv=a
    print(f'#{t+1} {maxv-b}')