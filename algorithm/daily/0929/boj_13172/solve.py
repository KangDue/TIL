import sys
sys.stdin = open('input.txt')
"""
sigma
상상의 n면체 주사위 던질 때,
각 면의 숫자가 주어지고, 각 면이 나올 확률이 같다면
이 값의 기댓값은 무한소수가 될 수도 있다.
M개의 주사위가 있어 이중 i번쨰 주사위는 Ni 면체 주사위 리를 더한값에 Si 일 때
모든 주사위를 각 한 번씩 던졌을때 나온 수들의 합의 기댓값을 구하는 문제.
s1/n1 + s2/n2 ..
이 모든 분수를 통분한다고 쳐보자
모듈러연산의 역원이 이해가 안되네
그냥 식이 나와있는걸 그대로 써서 ...
"""

from math import gcd,lcm #최소공배수, 최대 공약수
x = 1000000007
m = int(input())
N,S = [],[]
for _ in range(m):
    n,s = map(int,input().split())
    N.append(n)
    S.append(s)
parent = lcm(*N) #통분시 분모

child = sum(map(lambda x:S[x]*parent//N[x],range(m))) # 통분시 분자
gcd_k = gcd(child,parent)
b,a = parent//gcd_k, child//gcd_k
res = pow(b,x-2,x)
print((a*res)%x)


##### 1등참고 꼭 공부하자.!
import sys
input = sys.stdin.readline
M = int(input())
mod = 1000000007

mom,son = map(int,input().split())
for _ in range(M-1):
	mom_i, son_i = map(int,input().split())
	son = son*mom_i + mom*son_i
	mom = mom*mom_i
	son %=mod
	mom %=mod

final_mom=1
for i in bin(mod-2)[2:][::-1]:
	if i=='1':
		final_mom = final_mom*mom%mod
	mom = mom*mom%mod
print(son*final_mom%mod)