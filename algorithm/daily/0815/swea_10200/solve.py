import sys
sys.stdin = open('input.txt', encoding='utf-8')

a = []
for t in range(1, int(input())+1):
    n, A, B = map(int,input().split())
    minv = 0 if A + B <= n else A + B - n
    maxv = B if A > B else A
    a.append(f'#{t} {maxv} {minv}')
print(*a, sep="\n")