import sys
sys.stdin = open('input.txt', encoding='utf-8')

for t in range(1,int(input())+1):
    n = int(input())
    mat = [list(map(int,input().split())) for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i==0 and j == 0:
                continue
            elif i == 0: #일단 상단벽은 누적합 갱신
                mat[i][j] += mat[i][j-1]
            elif j == 0: #일단 좌측 벽은 누적합 갱신
                mat[i][j] += mat[i-1][j]
            else:#올수 있는 두가지 경로중 작은놈 고르기
                mat[i][j] += min(mat[i-1][j], mat[i][j-1])
    print(f'#{t} {mat[n-1][n-1]}')
