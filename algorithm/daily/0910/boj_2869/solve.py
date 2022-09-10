import sys
sys.stdin = open('input.txt')
"""
땅위 달팽이
낮에는 A 미터 올라가고
밤에는 B 미터 미끄러짐.
v미터 막대를 모두 올라가는데 며칠이 걸리는가?
V-A 를 A-B로 나눈 몫
"""
A,B,V=map(int,input().split())
a,b=divmod(V-A,A-B)
print((1+a+bool(b)) or 1)
# 가끔 python이 훨씬 빠른 경우가 있다.
# pypy 108ms
# python3 68ms

# 몫과 나머지 여부 계산은 (3//음수)의 절대값과 같다.
print(3//-2)