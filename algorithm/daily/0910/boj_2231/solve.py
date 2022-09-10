import sys
sys.stdin = open('input.txt')
# 분해합구하기
# 자기자신 + 1 ~ 자기자신 + 9 * n (자릿수)
origin = input()
n = int(origin)
l = len(origin)
def desum(x):
    ans = x
    while x:
        x,xx = divmod(x,10)
        ans += xx
    return ans
start = n-l*9 if n >= l*9  else 0
for i in range(start,n):
    if desum(i) == n:
        print(i)
        break
else:
    print(0)
