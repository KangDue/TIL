"""
무선 충전
index 1,1부터 시작 grid 주어짐. 10x10 크기
두 지점 사이 거리는 맨해튼
x,y 좌표로 주어짐 (r,c 반대임)
위치 범위 성능 줌
각 시간마다 1칸씩 이동
동시에 한 곳에 접속했다면 충전양 균등하게 분배한다.
(겹치는 곳이라면 서로 다른곳에서 충전하는게 효율적)
BC 정보주어짐
A = 1,1 B = 10,10 에서 출발
"""
import sys

sys.stdin = open('input.txt')

to = [[0,0],[-1,0],[0,1],[1,0],[0,-1]] #정지 상 우 하 좌
#시작위치에서부터 충전 가능^^
def move(y, x, path, arr, step=0):
    global T,visited
    if visited[y][x]:
        arr[step] = visited[y][x]
    if step==T:
        return 0
    ny = to[path[step]][0]+y
    nx = to[path[step]][1]+x
    move(ny,nx,path,arr,step+1)


for t in range(1,int(input())+1):
    T,A = map(int,input().split()) #총 이동시간, 충전소 개수
    #이동 경로 0 이동x, 1상, 2우, 3하, 4좌
    apath = [*map(int,input().split())]
    bpath = [*map(int, input().split())]
    bc = [[] for _ in range(9)]
    bp = [0]*9 #최대 8장소
    visited = [[[] for _ in range(11)] for _ in range(11)]
    for i in range(1,A+1):
        x,y,ran,pw = map(int,input().split())
        bc[i].append([y,x])
        bp[i] = pw
        q = [[y,x]]
        visited[y][x].append(i)
        step = 0
        while q and step < ran:
            step += 1
            new = []
            for r,c in q:
                for j in range(1,5):
                    ny = r + to[j][0]
                    nx = c + to[j][1]
                    if 1<=ny<=10 and 1<=nx<=10 and (i not in visited[ny][nx]):
                        visited[ny][nx].append(i)
                        new.append([ny,nx])
                        bc[i].append([ny,nx])
            q = new
    # print(bp)
    # print(bc)
    # print(*visited,sep='\n')
    at = [[0] for i in range(T+1)] # a 충전양 테이블
    bt = [[0] for i in range(T+1)] # b 충전양 테이블

    move(1,1,apath,at)
    move(10,10, bpath, bt)
    # print(at)
    # print(bt)

    maxv = 0
    for i in range(T+1):
        temp = 0
        for a in at[i]:
            for b in bt[i]:
                if a==b:
                    temp = max(temp,bp[a])
                else:
                    temp = max(temp, bp[a] + bp[b])
        maxv += temp
    print(f'#{t} {maxv}')






