import sys
sys.stdin = open('input.txt')
n = int(input())
for i in range(n):
    print(f'{"*"*(i+1):>{n}}')
