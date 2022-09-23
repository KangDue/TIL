from collections import defaultdict as dd
def tour(r,c):
    global mv
    for a in range(1,n-c):
        for b in range(1,c+1):
            if a+b < n-r:
                hist = dd(int)
                hist[grid[r][c]] = 1
                ny, nx = r, c
            try:
                for i,k in enumerate((a,b,a,b-1)):
                    for j in range(k):
                        ny += to[i][0]; nx += to[i][1]
                        if hist.get(grid[ny][nx]):raise Exception
                        hist[grid[ny][nx]] = 1
                else: mv = max(mv,len(hist)-1)
            except: pass
    return mv
for t in range(int(input())):
    n = int(input())
    grid = [[*map(int,input().split())] for _ in range(n)]
    to = [[1, 1],[1, -1], [-1, -1], [-1, 1]]
    mv = 0
    for r in range(n-2):
        for c in range(1,n-1):
            tour(r, c)
    if not mv:mv=-2
    print(f'#{t+1} {mv+1}')