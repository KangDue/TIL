import sys
sys.stdin = open('input.txt')

#게임 규칙을 잘못 이해, 중간에 바껴서 새로 먹을수 있는돌이 있으면 그것조차 다바뀐다. 완전탐색해야함.
def update(y,x,z):#grid 업데이트
    global grid
    #가로 세로 대각선 다살피기 #라고 생각하다가 라인별로 정로를 가지고 있다가 차근차근 갱신하면 안되나 ??? 라는 생각
    for i in dxy:
        row,col = y,x
        count = 0
        while grid[row+i[0]][col+i[1]]:#놓은곳 기준 한방향으로 쭉 이동
            count += 1
            row += i[0]
            col += i[1]
            if grid[row][col]==z:#색이 같으면 중간 싹다 바꾸기 -> 중간에 색이 같은 곳이 있다면 바꿔줘야함.(끝이 달라도 중간에 있을 수 있다.)
                for c in r(count):
                    grid[y+i[0]*c][x+i[1]*c]=z
                break

d,w,r=int,input,range
for t in r(d(w())):
    n,m = map(d,w().split()) #한변의 길이와, 돌 놓는 횟수 m
    #input은 x,y를 cartesian 좌료로줌. 행열에 적절하게 쓰려면 제로패딩 후에 [y][x]
    grid = [[0]*(n+2) for i in r(n+2)] # zero padding
    for i in r(2):
        for j in r(2):
            grid[n//2+i][n//2+j] = (i==j)+1 #흑돌이 1, 백돌이 2

    dxy=[[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]] #12시 기준 시계방향 8개 방위
    for i in r(m):
        y,x,z=map(d,w().split())
        grid[y][x]=z
        update(y,x,z)
    a=b=0
    for i in r(1,n+1):
        for j in r(1,n+1):
            if grid[i][j]==1:a+=1 #흑돌이면
            elif grid[i][j]==2:b+=1
    print(f'#{t+1}',a,b)