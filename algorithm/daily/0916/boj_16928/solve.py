import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(100000)
"""
뱀과 사다리 게임.
주사위를 맘대로 조작 가능하면 얼마나 빨리 도착점에
도달할까?
10x10 보드 1~100까지 적혀있음
주사위를 굴려 나온수 만큼 이동 가능
i에서 4면 i+4
사다리면 사다리 타고 올라가고(번호 증가) 뱀이면 뱀타고 내려감
1번출발 100번도착하기
뱀타면 무조건 손해
사다리 타면 무조건 이득 
최대 하나의 사다리 또는 뱀 !!!!!
"""
from collections import deque
n,m = map(int,input().split()) # 사다리, 뱀
ladder = dict() # x -> y 이동
snake = dict()
board = [0]*101
for i in range(n):#사다리는 증가, 뱀은 감소
    x,y=map(int,input().split())
    ladder[x] = y
for j in range(m):
    x,y=map(int,input().split())
    snake[x] = y
#사다리까지 뱀 안밟고 최단거리
#한 곳으로 가는 최단 경로가 여러가지 일 수도 있으니 - 이건 그런 경로 숫자 파악할때나 중요. 도착여부에는 고려 안해도됨.
#방문체크 위치를 바꿔줘야함. 뱀을 타고 가는게 빠를 수 도 있음.?
#사다리 타고 뱀을 밟고 사다리 밟고 등 ..
#핵심은 뱀을 밟아도 빨리 갈 수 있다!
q = deque([[1,0]])
board[1] = 1
while q:
    try:
        v,c = q.popleft()
        if v == 100:
            print(c)
            raise Exception
        for i in range(1,7):
            nv = v+i
            if nv <= 100 and not board[v+i]:
                temp = ladder.get(nv) or snake.get(nv) or nv
                board[temp] = 1
                q.append([temp,c+1])
    except:
        break
