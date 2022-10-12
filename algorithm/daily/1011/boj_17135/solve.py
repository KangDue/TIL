"""
캐슬 디펜스
NxM 격자판
각 칸에 적의수 최대 1,
N+1번행 모든 칸에는 성이 있다.
궁수는 성이 있는 칸에 배치가능(3명 배치, 하나의 칸 최대 1명)
턴 마다 각 궁수는 적 1명 공격 가능.
거리가 D 이하인 적 중 가장 가까운 녀석, 여럿이면 가장 왼쪽
공격받으면 제외, 공격이 끝나면 아래로 이동, 성이 있는칸으로 가도 제외,
모드 적에 격자판에서 제외되면 끝.
궁수로 제거 가능한 최대 적의 수는 ?
거리는 맨해튼

! 궁수의 공격이 끝나면 이동한다!
문제 풀이 45분 컷뜨... 문제를 꼼꼼하게 읽읍시다!
"""
import sys
sys.stdin = open('input.txt')

from itertools import combinations as cb
def md(pos1,pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])
R,C,D = map(int,input().split())
grid = [[*map(int,input().split())] for _ in range(R)]+[[-1]*(C)]
# print(*grid,sep='\n')
enemies = [] #초기 적 위치
for i in range(R):
    for j in range(C):
        if grid[i][j]:
            enemies.append((i,j))
can = []
for i in range(C):
    can.append((R,i)) #궁수 가능한 포지션

#문제를 잘 읽자 같은 적이 여러 궁수에게 공격 당할 수 있다. ( 동시 공격이라, 잡고 나머지 중 선택 x)
maxv = 0
for comb in cb(can,3):
    count = 0
    q = enemies[:]
    while q:
        new = []
        hunted = {}
        # 역시 정렬로 풀면 너무 느림 ㅋ;
        for i in comb: #각 궁수별 사냥
            temp = min(q,key=lambda x:(md(i,x),x[1]))
            if md(i,temp) <= D:
                if not hunted.get(temp):
                    hunted[temp] = 1
                    count+=1
        for y,x in q:#적 이동
            if hunted.get((y,x)):
                continue
            ny=y+1
            if ny == R: # 성 도착시 제외.
                continue
            else:
                new.append((ny,x))
        q=new
    maxv = max(maxv, count)
print(maxv)















