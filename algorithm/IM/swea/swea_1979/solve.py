import sys
sys.stdin = open('input.txt')

from functools import reduce as rd
d,w,r=int,input,range
for t in r(d(w())):
    n,k=map(d,w().split())
    g=[w().replace(' ','') for i in r(n)]
    g=rd(lambda x,y:x+y,[''.join(i).split('0') for i in zip(*g)]+[i.split('0') for i in g])
    print(f'#{t+1} {g.count("1"*k)}')