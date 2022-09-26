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
# nums = [0]+[3*2**i for i in range(11)]
# n = int(input())
# for i in range(10):
#     if n == 3*2**i:
#         break
# k,center = i, (n-1)
# grid = [[' ']*(2*n) for _ in range(n)]
# def make_trg(level = 0, center = n-1,side = 0): 재귀로 하려니까 잘 안되누 ;; 조건도 이상하게 먹히고
#     if level >= n:
#         return 0
#     if grid[level-1][center-1] == '*' and side == 1:
#         pass
#     if grid[level-1][center+1] == '*' and side == -1:
#         pass
#     else:
#         grid[level][center] = '*'
#         grid[level+1][center-1],grid[level+1][center+1]='*','*'
#         grid[level+2][center-2:center+3] = '*'*5
#
#         make_trg(level + 3, center + 3,1)  # 우측 끝
#         make_trg(level + 3, center - 3,-1)  # 좌측 끝
#
#         #다음은 center -3 , center +3 에서 시작.
# make_trg()



n = int(input())
for i in range(10):
    if n == 3*2**i:
        break
k,center = i, (n-1)
grid = [[' ']*(2*n) for _ in range(n)]
for level in range(0,n,3):
    for i in range(center-level,center+level+1,6):
        sc = grid[level - 1][i - 1:i + 2].count('*')
        if sc > 1:
            continue
        elif level and not sc:
            continue
        grid[level][i] = '*'
        grid[level + 1][i - 1], grid[level + 1][i + 1] = '*', '*'
        grid[level + 2][i - 2:i + 3] = '*' * 5
grid = [''.join(i) for i in grid]
print(*grid,sep='\n')

# ## 지리는 숏코딩...
# N=int(input())
# r=['*','* *','*'*5]
# i=6
# ###
# while i<=N:
#     r+=[s.ljust(i)+s for s in r]
#     i*=2
# for s in r:
#     print(s.center(i-1)) # 중앙정렬.