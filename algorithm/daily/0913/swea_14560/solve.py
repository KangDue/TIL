import sys
sys.stdin = open('input.txt')
"""
두 개의 변수 a와 b가 있다. 처음에 변수 a에는 정수 a0가, 
변수 b에는 정수 b0가 저장되어 있다. 단, a0 ≠ b0이다.
두 변수에 저장된 값을 바꾸는 방법은 아래 두 종류의 연산을 적용하는 것뿐이다.
  - 연산 X: a에 1을 더하고, b에 2를 곱한다.
  - 연산 Y: b에 1을 더하고, a에 2를 곱한다.
연산 과정에서 a와 b에 저장된 값이 굉장히 커질 수 있다.
 예를 들어 b=1인 상황에서 연산 X를 500번 적용하면 b에는 2500이 저장된다. 
당신은 이 두 연산을 원하는 순서대로 합쳐서 최대 1,000번까지 적용할 수 있으며, 
이를 통해 두 변수 a와 b에 같은 값이 저장되도록 하려고 한다. 
어떤 연산을 적용해야 하는지 구하는 프로그램을 작성하라.
1. 10100개 테스트케이스
"""
from collections import deque
from itertools import combinations as cb
X = lambda a,b:(a+1,b<<1)
Y = lambda a,b:(a<<1,b+1)
def rex(text):
    temp = ''
    for i in temp:
        if i == 'X': temp += 'Y'
        else: temp += 'X'
    return temp
# for tc in range(int(input())):

    a,b=map(int,input().split())
    ans = ''
    q = deque([[a,b,'']])
    while q:
        try:
            x,y,ops = q.popleft()
            for name,ex in (['X',X],['Y',Y]):
                na,nb = ex(x,y)
                if na == nb:
                    ans = ops + name
                    raise ValueError
                else:
                    q.append([na,nb,ops+name])
        except:break
    print(f'#{tc+1} {ans}')