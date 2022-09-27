import sys
sys.stdin = open('input.txt')
"""
치즈는 냉동보관해야 하는데 
실온에 두어서 녹고있다.
2변 이상이 공기와 접촉죽인 치즈는 한시간 뒤에 녹아 사라진다.
치즈 내부의 빈공간은 제외.
치즈가 모두 녹아 없어지는데 걸리는 시간은?
첫시도 시간초과
둘째시도 input방식 바꿨으나 시간초과 , 알고리즘 자체가 느림 ,.ㅠ
불필요한 집합의 삭제 및 재생성과정, 반복문, 할당, 비교연산 지움
계속 9퍼찍고 시간초과뜨노 ...;
왠지 치즈 내부 처리를 독바로 안해서 그냥 무한루프때운에 시간초과 뜬거같은 느낌!
어려운 문제도 아닌데 엄청 헤맸다.

차근차근 해결해야 하는 subproblem들을 생각하고 순서에 맞게 정리하자. DAG 같이(유향 비순환 그래프)
"""
#외부 공기는 가장 바깥 격자부터 bfs로 닿는 범위 전부임.
#나머지는 내부.
#외부에서 시작해서 지속적으로 공격하는건 어떨까? 는 아닌듯 ㅋ; 치즈 녹는 조건 구하기 힘듬



import time
start = time.time()


def check_side(i,j): #주어진 치즈에 대해 사방탐색
    s = 0
    temp = []
    for dy,dx in to:
        ny = i+dy; nx = j+dx
        s += visited[ny][nx]
        if inside.get((ny,nx)): #일단 내부 빈공간 임시저장
            temp.append((ny,nx))
    if s>1: #2변 이상 실온 접촉시
        ctemp.append((i,j)) #녹는 치즈 목록에 추가
        itemp.extend(temp) #지워지면 빈공간 개통 리스트에 넣기
        grid[i][j] = 0

from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
grid = [[*map(int,input().split())] for _ in range(n)]
visited = [[0]*m for _ in range(n)]
to = [[1,0],[-1,0],[0,1],[0,-1]]
q = deque([[0,0]])
visited[0][0] = 1
while q: # 4ms
    y,x = q.popleft()
    for dy,dx in to:
        ny = y+dy; nx = x+dx
        if 0<=ny<n and 0<=nx<m and not (visited[ny][nx] or grid[ny][nx]):
            visited[ny][nx] = 1
            q.append([ny,nx])
cheese = dict() #치즈 좌표 모음
inside = dict() #치즈 내부 좌표 모음
for y in range(n):  # 2ms
    for x in range(m):
        if not (visited[y][x] or grid[y][x]):
            inside[(y,x)] = 1
        elif grid[y][x]:
            cheese[(y,x)] = 1
i = 0
t = 0
ctemp,itemp = [],[]
ix=cx=0
while cheese:
    t += 1
    for i in cheese: # 치즈 체크
        check_side(i[0], i[1])
    for i in range(cx,len(ctemp)): #녹임처리
        y,x = ctemp[i]
        cheese.pop((y,x))
        visited[y][x] = 1
    for i in range(ix,len(itemp)): #개통 및 실온처리
        y,x = itemp[i]
        if inside.get((y,x)):
            inside.pop((y,x))
            visited[y][x] = 1
            q = deque([[y, x]])
            while q:
                r,c = q.popleft()
                for dy, dx in to:
                    ny = r + dy;
                    nx = c + dx
                    if inside.get((ny,nx)):
                        visited[ny][nx] = 1
                        q.append([ny, nx])
                        inside.pop((ny, nx))
    cx = len(ctemp)
    ix = len(itemp)
    i+=1
print(t)

end = time.time()
print('cost',round(end-start,6)*1000,'ms')
