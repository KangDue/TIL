import sys
sys.stdin = open('input.txt')

d,w,r=int,input,range
for t in r(d(w())):
    n=d(w());m=[[*map(d,w())] for i in r(n)];a=0
    for i in r(n):q=abs(n//2-i);a+=sum(m[i][q:n-q])
    print(f'#{t+1} {a}')