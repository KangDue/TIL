import sys
sys.stdin = open('input.txt')
"""
빙산이 녹고 있다.
빙산의 높이는 양의 정수이다.
빙산 외의 바다는 0이다.
빙산의 높이는 인접한 바다면(상하좌우)의 개수만큼씩 줄어든다.(매 스텝마다.)
0보다 더 작아지지는 않는다.
한덩어리의 빙산이 주어질때 빙산이 두 덩어리 이상으로 분리되는 최초시간 구하는 프로그램.
How?
1.반복문으로 주변의 갯수만큼 한 해씩 돌리면서 녹인다.
p2.그리고 영역판단때 자주 쓰던 check함수를 구현하여 영역의 개수를 구한다.
"""
from collections import deque
#다 녹아 사라질때까지 2덩이가 안되면 0 출력
R,C = map(int,input().split())
#크기 300x300 중 빙산 최대 10000개
#첫행열,마지막행열 항상 0이다.
grid = [[*map(int,input().split())] for _ in range(R)]
#처음부터 빙산좌표를 받아놓고 빙산들만 확인하는게 효율적일듯 하다.
#처음에 한덩이었다가 한덩이가 아니게되면 바로 ㄱ
ice = []
for y in range(R):
    for x in range(C):
        if grid[y][x]: ice.append([y,x,grid[y][x]])
#빙산이 전부 한구역이다 ? = 전부 거리가 manhattan 거리가 1이라는 뜻.
#녹이기랑 거리체크를 전부 ice에서 진행한다. 녹아서 사라지면 지워버림.
to = [[1,0],[-1,0],[0,1],[0,-1]]
def melt():
    now = -1
    dels = []
    for y,x,z in ice:
        now += 1
        for dy,dx in to:
            if grid[y+dy][x+dx] == 0:
                z -= 1
        if z<=0:
            dels.append(ice[now])#삭제할 놈들 추가
        else:
            ice[now][2] = z
    return dels
while 1:#녹이기 진행
    for i in melt():
        ice.remove(i)

















