import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    n,d = map(int,input().split())
    ans = n//(2*d+1)+1 if n%(2*d+1) else n//(2*d+1)
    print(f'#{t} {ans}')