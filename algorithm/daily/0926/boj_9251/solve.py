import sys
sys.stdin = open('input.txt')
"""
LCS(최장 공통 부분집합)
두 문장이 길이가 같다는 보장이 없어서 인덱스 에러뜸 .ㅠ
"""

a = input()
b = input()
la = len(a)
lb = len(b)
if la > lb: pivot = la
elif lb > la: pivot = lb
else: pivot = la
grid = [[0]*(pivot+1) for _ in range(pivot+1)]
a = '0' + a
b = '0' + b

for i in range(1,pivot+1):
    for j in range(1,pivot+1):
        try:
            if a[i] == b[j]:
                grid[i][j] = grid[i-1][j-1] + 1
            else:
                grid[i][j] = max(grid[i-1][j], grid[i][j-1])
        except:
            pass
print(max(sum(grid,[])))