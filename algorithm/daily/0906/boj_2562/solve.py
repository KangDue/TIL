import sys
sys.stdin = open('input.txt')
maxv=[0,-1]
for i in range(9):
    n=int(input())
    if maxv[0] < n:
        maxv=[n,i+1]
print(*maxv,sep='\n')