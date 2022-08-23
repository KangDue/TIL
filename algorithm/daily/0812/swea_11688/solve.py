import sys

sys.stdin = open('input.txt', encoding='utf-8')

import math
T = int(input())
#root 1/1 의 자식노드 구하기
for t in range(1,T+1):
    child = input()
    a, b = 1, 1
    for i in child:
        if i == "L":
            a, b = a, a+b
        else:
            a, b = a+b, b
    #사실상 기약분수 만들기 문제
    deno = 2
    pivot = a if a>b else b
    a //= math.gcd(a, b)
    b //= math.gcd(a, b)
    # 유클리디안 호제법도 있으나 그냥 모듈쓰자
    # 아래 방식은 시간초과 떠버림. pythonic하게 가자
    # while deno <= pivot: #숫자 그리 크지 않음
    #     if a%deno == 0 and b%deno == 0:
    print(f'#{t}',a,b)
