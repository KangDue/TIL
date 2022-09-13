import sys
sys.stdin = open('input.txt')
"""
중위순회로 문자읽기
"""


def io(x):
    global ans
    if t[x][1]: io(I(t[x][1]))
    ans += t[x][0]
    if t[x][2]: io(I(t[x][2]))
I,R,W=int,range,input
for tc in R(10):
    n=I(W())
    t=[[0,0,0] for _ in R(n+1)]
    for _ in R(n):
        a,*b=W().split()
        for k in R(len(b)):t[I(a)][k]=b[k]
    ans='';io(1);print(f'#{tc+1} {ans}')