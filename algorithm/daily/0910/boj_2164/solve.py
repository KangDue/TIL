import sys
sys.stdin = open('input.txt')

from collections import deque
n = int(input())
q = deque(list(range(1,n+1)))
mode = 1
while len(q) != 1:
    if mode: q.popleft(); mode ^= 1
    else: q.append(q.popleft()); mode ^= 1
print(q.pop())

# g리는 규칙
# a,b=int(input()),1
# while a>b:b*=p2
# print(a*p2-b)