import sys
sys.stdin = open('input.txt')
"""

"""


def post(x):
    if x > n: return 0
    post(2 * x)
    post(2 * x + 1)
    if not values[x] and 2 * x + 1 < n + 1:
        values[x] = values[2 * x] + values[2 * x + 1]
    elif not values[x] and 2 * x < n + 1:
        values[x] = values[2 * x]
for t in range(int(input())):
    n,m,l = map(int,input().split())
    values = [0] * (n+1)
    for i in range(m):
        x,y = map(int,input().split())
        values[x] = y
    post(1)
    print(f'#{t+1} {values[l]}')