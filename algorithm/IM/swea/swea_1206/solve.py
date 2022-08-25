import sys
sys.stdin = open('input.txt')

d,w,r,l=int,input,range,list
for t in r(10):
    n = d(w())
    f = l(map(d,w().split()))
    f = l(filter(lambda x: x>0,map(lambda x:f[x]-max(f[x-1],f[x-2],f[x+1],f[x+2]),r(2,n-2))))
    print(f'#{t+1} {sum(f)}')