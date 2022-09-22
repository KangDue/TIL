import sys
sys.stdin = open('input.txt')
"""
유기농 배추
흰배추 지렁이가 해충방지에 효과적
지렁이들은 인접한 상하좌우로 이동가능하다.
그림 몇개인지 세고 영역 크기 파악하는 문제와 비슷
결론: 연결된 배추그룹에 지렁이 1마리만 있으면되니까
    필요한 최소 지렁이 수를 출력하라

How?
1.돌면서 1(배추)발견시마다 bfs실행 
p2.연결된 1들은 싹다 방문처리하고 배추벌레 카운트 1증가
3.반복
"""
from collections import deque
for t in range(int(input())):
    C,R,N = map(int,input().split())#가로,세로,배추개수
    cabs = [[*map(int,input().split())] for i in range(N)]
    #굳이 bfs가 아니어도 풀릴듯 하지만 일단 걍 풀자 ^^
    farm = [[0 for _ in range(C)] for _ in range(R)]
    for x,y in cabs: #입력데이터 형태 확인 할 것!
        farm[y][x] = 1
    visited = [[0 for _ in range(C)] for _ in range(R)]
    to = [[1,0],[-1,0],[0,-1],[0,1]]
    bugs = 0
    for i in range(R):
        for j in range(C):
            if farm[i][j] == 1 and visited[i][j] == 0:#방문한적 없는 배추
                bugs += 1
                q = deque([[i,j]])
                visited[i][j] = 1
                while q:#연결된 곳 전부 방문
                    y,x = q.popleft()
                    for dy,dx in to:
                        ny = y+dy; nx = x + dx
                        if 0<=ny<R and 0<=nx<C and visited[ny][nx] == 0 and farm[ny][nx] == 1:#배추일때 라는 조건 빠뜨리지 말자
                            visited[ny][nx] = 1
                            q.append([ny,nx])
    print(bugs)


