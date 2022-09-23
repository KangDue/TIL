import sys
sys.stdin = open('input.txt')
"""
별찍기!
N 은 항상 3×2**k 인수 , 
k = 0 일때 1 3 5 인 삼각형 하나(중간은 비었음)
k = 1 일때 삼각형 2
k = 2 일때 삼각형 2, 4개
k = 3 일떄 삼각형 2, 4, 8 개 (끝에서 부터 채움.
시작하는 가장 중간점 위치 (n - 1)//2
width = n * 2
"""
n = int(input())
for i in range(10):
    if n == 3*2**i:
        break
k,center = i, (n-1)
grid = [[' ']*(2*n) for _ in range(n)]
def make_trg(level = 0):
    for i in range(n):
        grid[level][center] = '*'
        grid[level+1][center-1],grid[level+1][center+1]='*','*'
        grid[level+2][center-2:center+3] = '*'*5



make_trg()
grid = [''.join(i) for i in grid]
print(*grid,sep='\n')
