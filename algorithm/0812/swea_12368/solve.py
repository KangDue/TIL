import sys
sys.stdin = open('input.txt')
T = int(input())
for t in range(1,T+1):
    a, b = map(int,input().split())
    print(f'#{t} {(a+b)%24}')
#1단계 수준인거 같은데 왜 3단계지??