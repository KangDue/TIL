import sys
sys.stdin = open('input.txt')
while 1:
    s = sorted([*map(int,input().split())])
    if s[0]==s[1]==s[2]==0:
        break
    if s[-1]*s[-1] == s[0]*s[0]+s[1]*s[1]:
        print("right")
    else:
        print("wrong")

# 별의 별 방법으로 다 줄이네
# a=1
# while a:
#   a,b,c=sorted(map(int,input().split()))
# a>0==print('rwirgohntg'[a*a+b*b!=c*c::p2])
