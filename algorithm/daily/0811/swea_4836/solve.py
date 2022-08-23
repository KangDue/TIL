import sys
sys.stdin = open('input.txt')
#10x10 grid 상 r,b color 좌상,우하 좌표로 사각형
#좌표가 그냥 cartesian 이 아니라 marix index 처럼하니 주의... 2,2, 4,4 넓이 = 9
#을 나타낼때 둘이 겹쳐 purple이 되는 영역 넓이 구하기
#그리드 1x1은 넓이 1
def fill(cord,grid):
    for i in range(cord[0],cord[2]+1):
        for k in range(cord[1],cord[3]+1):
            #좌표랑 행열 인덱스 반대임
            if grid[k][i] == cord[4]: #같은색이면 패스
                pass
            else:
                grid[k][i] += cord[4] # 다른색이면 덧칠
    return grid

T = int(input())
for t in range(1,T+1):
    n = int(input()) # 사각형 수
    grid = [[0 for i in range(11)] for k in range(11)] # 계산 편하게 11x11로 생성
    recs = [ list(map(int,input().split())) for i in range(n)]
    for i in recs:
        grid = fill(i,grid)
    ans = 0
    for i in grid:
        ans += i.count(3)
    print(f'#{t} {ans}')
