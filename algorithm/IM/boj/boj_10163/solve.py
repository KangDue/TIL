import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
색종이 
"""
if __name__ == "__main__":
    import sys
    sr = sys.stdin.readline
    n=int(sr())
    grid = [[0 for i in range(1001)] for j in range(1001)]#색종이를 받고 만들어서 범위 줄이기도 가능하지만 귀찮으니 pass
    for num in range(1,n+1):
        row,col,rh,cw=map(int,sr().split())
        for i in range(row,row+rh):
            for j in range(col,col+cw):
                grid[i][j] = num #색종이 번호 입력, 칠하기
    nums=[0]*(n+1)
    for i in range(1001):
        for j in range(1001):
            nums[grid[i][j]] += 1
    print(*nums[1:])
