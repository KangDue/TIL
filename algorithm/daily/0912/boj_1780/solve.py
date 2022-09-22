import sys
sys.stdin = open('input.txt')
"""
종이의 개수
1. 종이는 -1,0,1 중 하나로 이루어진 matrix
p2. 모두 같은수면 그대로 사용
3. 아니면 종이를 같은 크기의 종이 9개로 자르고(like sudoku)
    각각에 대해 p2 ~ 3반복
4. 이렇게 했을때 -1으로만, 0으로만, 1으로만 채워진 종이의 개수 출력
"""
n=int(input())
grid = [[*map(int,input().split())] for _ in range(n)]
count = [0,0,0] #0 1 -1
def paper(r,c,n):
    global grid,count
    pivot = grid[r][c]
    flag = False
    if n==1:
        count[pivot-2] += 1
        return 0
    for i in range(r,r+n):
        for j in range(c,c+n):
            if grid[i][j] != pivot:
                for y in range(r, r+n, n // 3):
                    for x in range(c, c+n, n // 3):
                        paper(y, x, n // 3)
                flag = True
                break
        if flag:
            break
    else:#정상종료시(다 같은 숫자면)
        count[pivot-2] += 1
        return 0
paper(0,0,n)
print(*count,sep='\n')