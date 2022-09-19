import sys
sys.stdin = open('input.txt')
"""
이진탐색
"""

def bisect(a,x):
    l = 0
    r = len(a)-1
    flag=-1
    while l!=r:
        m = (l+r)//2
        if a[m] == x: return 1
        elif x < a[m]:
            r = m-1
            if flag!=1:flag=1
            else:return 0
        elif x > a[m]:
            l=m+1
            if flag!=0 :flag=0
            else : return 0
        else: return 0
    if a[l] == x:
        return 1
for t in range(int(input())):
    n,m = map(int,input().split())
    a = sorted([*map(int,input().split())]) #정렬 된상태로 주어진줄알고 계속하다가 시간만 버렸네 ...
    b = [*map(int,input().split())]
    c = 0
    for i in b:
        temp = bisect(a,i)
        if temp: c+=1
    print(f'#{t+1} {c}')