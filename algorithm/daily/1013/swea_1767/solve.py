"""
프로세서 연결
"""
import sys

sys.stdin = open('input.txt')

to = [[1,0],[0,1],[-1,0],[0,-1]]
for t in range(int(input())):
    n = int(input())
    grid = [[3]*(n+2)] + [[3]+[*map(int,input().split())]+[3] for _ in range(n)] + [[3]*(n+2)]
    visited = [[0] * (n+2) for _ in range(n+2)]
    chip = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            if grid[i][j]:
                chip.append((i,j))
    lc = len(chip)

    # print(chip)
    ans = [0,int(1e9)]
    def dfs(idx=0,count=0,length=0):
        global lc,grid,ans
        if idx == lc:
            if count > ans[0]:
                ans = [count,length]
            if count == ans[0] and length < ans[1]:
                ans = [count,length]
            return 0
        if ans[0] > count+(lc-idx):
            return 0
        for dy,dx in to:
            sy, sx = chip[idx]
            flag = 0
            temp = []
            cnt = 0
            while 1: #전선 이어주기
                sy, sx = sy + dy, sx + dx
                if not grid[sy][sx]: #0이면 ㄱㄱ
                    temp.append((sy, sx))
                    continue
                elif grid[sy][sx] == 1 or grid[sy][sx] == 9: #0이아닌데 1보다 큰거 만나면 못이으니 종료
                    break
                elif grid[sy][sx] == 3: #-1이면 연결 성공
                    flag = 1
                    for r,c in temp:
                        cnt+=1
                        grid[r][c] = 9
                    break
            #print(idx,count,flag,length,cnt)
            dfs(idx+1,count+flag,length+cnt)
            if flag: #방문기록 해버렸다면
                while temp:
                    r,c = temp.pop()
                    grid[r][c] = 0

    dfs()
    print(f'#{t+1} {ans[1]}')






