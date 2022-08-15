import sys
sys.stdin = open('input.txt',encoding='utf-8')

a = []
for t in range(1, int(input())+1):
    p,q = map(float,input().split())
    ans = "YES" if (1-p) < p*(1-q) else "NO"
    a.append(f'#{t} {ans}')
print(*a, sep="\n")