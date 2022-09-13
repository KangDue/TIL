import sys
sys.stdin = open('input.txt')
"""
잉카제국이 카잉제국 토대로 세워졌다는 사실을 발견!
이들은 M,N보다 작거나 같은 두 자연수 x,y를 가지고 각 년도를 <x:y>의 형식으로 표현
첫 해를 <1:1> , 2번째 해 <2:2>
<x:y>의 다음 해는 <x':y'>일때 x,y가 각각 m,n보다 커지면 1로 돌아가서 시작한다.
<m:n>은 달력의 마지막 해로 이 때 종말이 온다는 예언이 있다.
시계같은 문제인듯 
x,y가 주어질때 이게 몇번째 해인지 구하고 불가능하면 -1 출력
"""
from math import lcm
for t in range(int(input())):
    m,n,x,y = map(int,input().split())
    l = max((m,x),(n,y))
    maxv = lcm(m,n)+1
    rm = range(1,m+1)
    rn = range(1,n+1)
    for c in range(0,maxv,l[0]): #모두 조사하면 시간 낭비하니, x또는 y 기준으로 무조건 가능한 값만 고르기
        c += l[1]
        if rm[c%m-1] == x and rn[c%n-1] == y and c < maxv: #무식하게 나머지연산 갈기면 idx하는 값이 정확히 일치하지 않음.
            print(c);break
    else:
        print(-1)