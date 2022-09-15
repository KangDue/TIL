import sys
sys.stdin = open('input.txt')
print(*divmod(*map(int,input().split())),sep='\n')