import sys
sys.stdin = open('input.txt')

d,w,r,s,p=int,input,range,set,print
for t in r(d(w())):#과제 제출안한사람 오름차순
    n,m=map(d,w().split()) #수강생수, 제출한사람수
    a=s(r(1,n+1))-s(map(d,w().split()))
    p(f'#{t+1}',end=" ")
    p(*a)