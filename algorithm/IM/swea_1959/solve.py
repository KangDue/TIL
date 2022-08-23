import sys
sys.stdin = open('input.txt')


from functools import reduce
d,w,l,r=int,input,list,range
for t in r(d(w())): #m이 더큰 수열, n이 작은수열
    n,m=map(d,w().split())
    a,b=l(map(d,w().split())),l(map(d,w().split()))
    if n > m: n,m=m,n;a,b=b,a
    maxv= -1000000
    for i in r(m-n+1):
        c=reduce(lambda x, y: x + y, map(lambda x: x[0] * x[1], zip(a,b[i:i+n])))
        if maxv<c:maxv=c
    print(f'#{t+1} {maxv}')