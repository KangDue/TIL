import sys
sys.stdin = open('input.txt')

from collections import deque as q
w=input
for t in range(10):
    w();n=q([*map(int,w().split())]);c=q([1,2,3,4,5])
    while n[-1] > 0:n[0]-=c[0];n.rotate(-1);c.rotate(-1)
    n[-1]=0;print(f'#{t+1}',*n)