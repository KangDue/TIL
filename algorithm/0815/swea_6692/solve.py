import sys
sys.stdin = open('input.txt',encoding='utf-8')

from functools import reduce
a = []
for t in range(1, int(input())+1):
    n = int(input())
    prob = [0]+[input().split() for i in range(n)] #싹다 float으로 받으면 렉걸림.
    prob = reduce(lambda x,y: x + float(y[0])*int(y[1]),prob)
    a.append(f'#{t} {prob}')
print(*a)