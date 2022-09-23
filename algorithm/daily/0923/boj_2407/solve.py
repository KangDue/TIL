import sys
sys.stdin = open('input.txt')
"""
조합
"""

from math import factorial as fac
n,m = map(int,input().split())
# print(comb(n,m))#모듈 버전
print(fac(n)//fac(m)//fac(n-m))

# 아래는 백준 시간 1등. 이런 규칙이 있단다.
# 파스칼의 삼각형 대칭인것을 생각하면 맞음 ㅇㅇ
# 6개중 4개를 뽑는 경우의 수 = 6개중 2개를 안뽑는 경우의 수
inp=input().split()
n = int(inp[0])
m = int(inp[1])
if n-m<m: #계산수 절감
	m=n-m
r=1
for i in range(m): #반복문으로 팩토리얼
	r=r*(n-i)//(i+1)
print(r)