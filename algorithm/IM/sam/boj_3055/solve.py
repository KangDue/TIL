import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
탈출
비버의굴 D
고슴도치 S
물찬곳 * 물은 매 초마다 퍼진다. 인접구역으로 (돌,비버굴,고슴도치 제외)
돌 X
인접한 상하좌우로 한칸씩 이동가능
R행 C열
고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다 .
set으로 중복을 줄여도 yield로 메모리를 아껴도 계속 ,, 메모리 초과
종료조건을 손보자.
"""
if __name__ == "__main__":
    import sys
    sr = sys.stdin.readline
    from collections import deque
    def flood():#홍수 일어나는 함수
        #반복문마다 바꾸면 중복해서 더바꿔버림 좌표만 기억하자
        if before == now: # 1분마마다 홍수 발생
            temp = set()
            for i in range(R):
                for j in range(C):
                    if road[i][j] == '*': # 물이 찬 곳
                        for dy,dx in to:
                            y = i+dy; x = j+dx
                            if 0 <= y < R and 0 <= x < C: #범위확인
                                if road[y][x] == '.': #멀쩡한 길이면 침수시킴
                                    temp.add((y,x))
            for y,x in temp:
                road[y][x] = '*'

    R,C = map(int,sr().split())
    road = [[*sr().strip()] for i in range(R)]
    for i in range(R):
        for j in range(C):
            if road[i][j] == 'S':
                S = [i,j]
            if road[i][j] == 'D':
                D = [i,j]
    q = deque([[S[0],S[1],0]])#위치,
    visited = [[0 for i in range(C)] for j in range(R)]
    visited[S[0]][S[1]] = 1
    to = [[1,0],[-1,0],[0,1],[0,-1]]
    before = 0
    while q:
        y,x,now = q.popleft()
        if now == before:#다음시간대 홍수 예측
            flood();before += 1
        if road[y][x] == 'D':#찾으면 종료
            print(now)
            break
        for dy, dx in to:
            ny = y+dy; nx = x+dx #유효범위고 방문한적이 없다면
            if 0<= ny < R and 0<= nx < C and visited[ny][nx] == 0:
                if road[ny][nx] not in '*X':#물넘친곳이나 돌이 아닌곳으로만 무빙 가능.
                    q.append([ny,nx,now+1])
                    visited[ny][nx] = 1
    else:
        print("KAKTUS")


        # c = 0
        # block = 0
        # for dy, dx in to:
        #     ny = D[0] + dy; nx = D[1] + dx
        #     if 0 <= ny < R and 0 <= nx < C:
        #         c += 1  # D 주변 범위 카운트, 길, 물, 돌
        #         if road[ny][nx] in '*X':#돌,물등 막혀있는지 카운트
        #             block += 1
        # if c==block:#둘러 쌓여있으면 어차피 못감
        #     print("KAKTUS")
        #     break