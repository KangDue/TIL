import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    n,m = map(int,input().split()) # + 또는 x 방향으로 각 m칸
    fly = [[*map(int,input().split())] for i in range(n)]
    def pfly(i,j):# + 모양
        to = [[1,0],[-1,0],[0,-1],[0,1]]
        temp = fly[i][j]
        for dy,dx in to:
            y = i+dy; x= j+dx; c = 0
            while 0<= y < n and 0<= x < n and c < m-1:
                temp += fly[y][x]
                y+=dy; x+=dx
                c += 1
        return temp
    def xfly(i,j):# x 모양
        to = [[1,1],[1,-1],[-1,1],[-1,-1]]#대각선 방향
        temp = fly[i][j]
        for dy,dx in to:
            y = i+dy; x= j+dx; c = 0
            while 0<= y < n and 0<= x <n and c < m-1:
                temp += fly[y][x]
                y+=dy; x+=dx
                c += 1
        return temp
    maxv = 0
    for i in range(n):
        for j in range(n):
            maxv = max(pfly(i,j),xfly(i,j),maxv)
    print(f'#{tc+1} {maxv}')