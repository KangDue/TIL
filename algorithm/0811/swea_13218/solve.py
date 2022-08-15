import sys
sys.stdin = open('input.txt')
T = int(input())
for t in range(1,T+1):
    n = int(input())//3
    print(f"#{t} {n}")