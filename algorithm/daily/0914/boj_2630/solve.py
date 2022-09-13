import sys
sys.stdin = open('input.txt')
"""
색종이 만들기
정사각형들은 파란색 또는 하얀색으로 이루어져 있다.
전체 종이는 NxN이고 N = 2**k
전체가 모두 같은색이 아니면 4분할한다.
계속 반복해 나간다. 
색깔별 종이가 몇장인지 출력하자
흰색은 0, 파란색은 1
첫째줄에는 파란색, 둘재줄에는 파란색
"""
n = int(input())
grid =[[*map(int,input().split())] for _ in range(n)]
paper = [0,0]
def make(r,c,n):
    pivot = grid[r][c]
    if n == 1:
        paper[pivot] += 1
        return 0
    for y in range(r,r+n):
        for x in range(c,c+n):
            if grid[y][x] != pivot:
                for ny in range(r,r+n,n//2):
                    for nx in range(c,c+n,n//2):
                        make(ny,nx,n//2)
                return 0
    else:#전부 같은 색이라면
        paper[pivot] += 1
make(0,0,n)
print(*paper,sep='\n')


