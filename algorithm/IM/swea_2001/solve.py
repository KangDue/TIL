import sys
sys.stdin = open('input.txt')

d,w,r=int,input,range
def chae():
    x=0
    for a in r(m):
        for b in r(m):
            x+=f[i+a][j+b]
    return x
for t in r(d(w())):
    n,m = map(d,w().split()) #mxm 파리채로 파리잡기 최소값
    f = [list(map(d,w().split())) for i in r(n)]
    mv = 0
    for i in r(n-m+1):
        for j in r(n-m+1):
            x=chae()
            if mv<x:mv=x
    print(f'#{t+1} {mv}')