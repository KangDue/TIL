import sys
sys.stdin = open('input.txt')
for t in range(int(input())):
    a,b = map(int,input().split())
    print(a+b)
