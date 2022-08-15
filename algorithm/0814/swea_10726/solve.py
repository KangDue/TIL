import sys
sys.stdin = open('input.txt',encoding='utf-8')

a = []
for t in range(1, int(input())+1):
    n,m = map(int,input().split())
    ans = "ON" if f'{m:0b}'[-n:] == "1"*n else "OFF"
    a.append(f'#{t} {ans}')
print(*a, sep="\n")