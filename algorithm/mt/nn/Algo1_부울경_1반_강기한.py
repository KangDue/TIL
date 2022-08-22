def kabs(x): #절대값을 반환하는 함수
    if x > 0:
        return x #0보다 크면 그대로
    else:
        return -x #아니면 - 해서 반환

def mnr(r1,c1,r2,c2): #평탄화 영역의 평균높이를 구하고 답을 구하는 함수
    global grid
    ans = c = 0 # ans는 영역의 높이를, c는 영역별 필요한 평탄화 작업 수를 받아온다.
    for i in range(r1,r2+1):#끝점도 포함해야하니 + 1
        for j in range(c1,c2+1):
            ans += grid[i][j] #각 영역의 높이를 더한다.
    m = ans//((r2-r1+1)*(c2-c1+1)) #펑균값을 구한다.
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            c += kabs(m-grid[i][j]) #각 평탄화 지역별 필요한 작업 수를 더한다.
    return c

for t in range(1,int(input())+1):
    n = int(input())
    r1, c1, r2, c2 = map(int,input().split())
    grid = [list(map(int,input().split())) for i in range(n)]
    print(f'#{t} {mnr(r1, c1, r2, c2)}')
