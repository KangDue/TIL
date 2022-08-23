import sys
sys.stdin = open('input.txt')


def make_grid(i, k, color="#"):
    global n, m
    tile = {"#": '.', ".": "#"}
    start = tile[color] if k % 2 else color  # 홀수 열이면
    origin = tile[start] if i % 2 else start
    p1 = (origin + tile[origin]) * (m // 2) + origin if m % 2 else (origin + tile[origin]) * (m // 2)
    p2 = (tile[origin] + origin) * (m // 2) + tile[origin] if m % 2 else (tile[origin] + origin) * (m // 2)
    mode = True
    grid = []
    for i in range(n):
        if mode:
            grid.append(p1)
            mode = False
        else:
            grid.append(p2)
            mode = True
    return grid

T = int(input())
for t in range(1,T+1):
    n,m = map(int,input().split())
    grid = [input() for i in range(n)]

    posibility = True
    for i in grid:
        temp = i[::2]
        sharp, dot = temp.find("#"), temp.find(".")
        if sharp > -1 and dot > -1: #둘다 있는 경우만 impossible함
            posibility = False
            break #

    #하나라도 #이나 .이 나오면 전체가 결정됨.
    for i in range(n):
        if grid[i].find("#") > -1: #있다면
            a,b,c = i,grid[i].find("#"),"#"
        elif grid[i].find(".") > -1:
            a,b,c = i, grid[i].find("."),"."

    grid_com = make_grid(a,b,c)
    print(grid_com)
    print(grid)
    end = False
    for i in range(n):
        for k in range(m):
            if grid_com[i][k] != grid[i][k]:
                if grid[i][k] == "?":
                    pass
                else:
                    print(f"#{t} impossible")
                    end = True
                    break
        if end:
            break
    else:
        print(f"#{t} possible")
