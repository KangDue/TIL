import sys
sys.stdin = open('input.txt')

d,w,p=int,input,print
c={50000:0,10000:0,5000:0,1000:0,500:0,100:0,50:0,10:0}
for t in range(d(w())):
    n = d(w())
    for k in c.keys():
        c[k],n=divmod(n,k)#몫,나머지 반환
    p(f'#{t+1}')
    p(*c.values())