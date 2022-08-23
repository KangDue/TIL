import sys
sys.stdin = open('input.txt')

x,y,r=int,input,range
for t in r(1,11):
    n,l=x(y()),sorted(map(x,y().split()))
    for i in r(n):l[-1]-=1;l[0]+=1;l.sort()
    print(f'#{t} {l[-1]-l[0]}')