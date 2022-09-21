import sys
sys.stdin = open('input.txt')
"""
곱셈
A를 B번 곱한수를 C로 나눈 나머지
수 자체가 너무 커져도 연산에 속도가 느려진다!
"""
import sys
a,b,c=map(int,sys.stdin.readline().split())

def pow(x,a):
    if a == 1: return x%c
    else:
        t = pow(x,a//2)
        if a%2:
            return (t*t*x)%c
        else:
            return (t*t)%c
if b: print(pow(a,b))
else: print(a%c)