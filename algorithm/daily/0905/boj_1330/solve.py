import sys
sys.stdin = open('input.txt')
a,b=map(int,input().split())
if a>b:print('>')
elif a==b:print('==')
else: print("<")