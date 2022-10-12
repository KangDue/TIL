"""
색종이 붙이기
1x1~ 5x5 까지 다섯 종류 색종이 있음, 각 5개씩 가지고 있다.
10x10 종이에 1이 적힌 부분을 가지고있는 종이로 덮어야 한다.
가릴 수 있는 최소 종이 개수는?
다 덮는게 불가능하면 -1
색종이와 덮는 1들의 경계가 일치해야 한다.
# 1차시도 1퍼부터 틀림 ㅋ; 범위 실수 (21분 경과)
# 2차시도 21퍼. (23분경과)
# 3차시도 그대로, (32분경과) ? 갑자기 번뜩, <경계> 가 일치 해야함. (경계만 일치해도 된다.) - 가 아니네; 0에는 색종이 x
# 4차시도 17퍼? 뭐지? (44분 경과)
# 5차시도 21퍼에서 틀림 ;
# 6차시도 21퍼에서 틀림 ; 모든 순열 브루트 포스 갈겨도 틀리는데..
#----- 수많은 시도 후, 빡쳐서 youtube 재귀, 백트래킹 강의보고
생각 정리후 깨달음?을 얻어 클리어
"""
import sys
sys.stdin = open('input.txt')

import time
def check(r, c, size):
    global grid
    count = 0
    for i in range(r, r + size):
        for j in range(c, c + size):
            if grid[10*i+j]:
                count += 1
    if count == size*size:  # 경계선 일치하면
        return count
    else:
        return 0

myp = [5]*6
grid = sum([[*map(int,input().split())] for _ in range(10)],[])
# print(*grid,sep='\n')
tot = 0
for r in range(10):
    for c in range(10):
        if grid[10*r+c]:
            tot += 1
            end = 10*r+c
minv = 1<<20
def dfs(y=0,x=0,step=0):
    global minv
    if y == 10:
        minv = min(minv,step)
        return 0
    elif x>=10: #다음행
        dfs(y+1,0,step)
    elif step >= minv: #커팅
        return 0
    else:
        if grid[10*y+x]: # 1이 시작 되면
            for size in range(5,0,-1): # size별 확인.
                if x+size <= 10 and y+size <= 10:
                    count = check(y,x,size)
                    if count and myp[size]: #가진 색종이로 카바 가능하면?
                        myp[size] -= 1
                        for i in range(y, y + size): #값을 잘봐라.. 자꾸 실수로 이상한값 넣어서 디버그하고있네
                            for j in range(x, x + size):
                                grid[10 * i + j] = 0
                        dfs(y,x+size,step+1)
                        myp[size] += 1
                        for i in range(y, y + size):
                            for j in range(x, x + size):
                                grid[10 * i + j] = 1
        else:# 1이 아니면 다음칸 확인
            dfs(y,x+1,step)
dfs()
if minv == 1<<20:
    print(-1)
else:
    print(minv)



