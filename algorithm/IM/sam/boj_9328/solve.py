import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
보통 메모리 초과는 종료조건 ...
열쇠
상근이가 훔칠 수 있는 문서의 최대 개수
. 길, * 벽, $ 문서, 대문자 = 문, 소문자 = 키
키는 자신의 대문자 문 전부 열 수 있다.
바닥에서 주울 수 도 있다.
훔칠 수 있는 문서의 최대 개수!
"""
if __name__ == "__main__":
    import sys
    sr = sys.stdin.readline
    from collections import deque
    for t in range(int(sr())):
        R,C = map(int,sr().split())
        maze = [['.']+[*sr().strip()]+['.'] for i in range(R)]
        maze = [['.']*(C+2)] + maze + [['.']*(C+2)]
        sk = {i:1 for i in sr().strip()}
        to = [[1,0],[-1,0],[0,-1],[0,1]]
        docs  = []
        for i in range(R+2):
            for j in range(C+2):
                if maze[i][j] == '$':
                    docs.append([i,j])
        q = deque([[0,0]])

        newk = False
        count = 0
        def bfs():
            global count,sk
            q = deque([[0, 0]])
            visited = [[0 for i in range(C+2)] for j in range(R+2)]
            while q:
                y,x = q.popleft()
                for dy,dx in to:
                    ny = y+dy; nx = x+dx
                    if 0<=ny<R+2 and 0<=nx<C+2:
                        if visited[ny][nx] != 1 and visited[ny][nx] != '*':#no방문
                            if maze[ny][nx].isupper() and sk.get(chr(ord(maze[ny][nx])+32)):#문이고 키가 있다면
                                visited[ny][nx] = 1
                                q.appendleft([ny,nx])
                                maze[ny][nx] = '.' #열었으니 길로 바꾸기
                            elif maze[ny][nx].islower(): #키 추가되면 초기화
                                sk[maze[ny][nx]] = 1
                                visited[ny][nx] = 1
                                maze[ny][nx] = '.' #주웠으니 길로 바꾸기
                                q = deque([[ny,nx]])
                                visited = [[0 for i in range(C + 2)] for j in range(R + 2)]
                            elif maze[ny][nx] == '$': #문서를 찾으면 .으로 바꾸고 1추가
                                q.append([ny, nx])
                                visited[ny][nx] = 1
                                count += 1
                                maze[ny][nx] = '.' # 주웠으니 길로 바꾸기
                            elif maze[ny][nx] == '.':#길이면
                                q.append([ny, nx])
                                visited[ny][nx] = 1

        bfs() #키 새로 추가 안될때까지 반복
        # print(*maze, sep='\n')
        print(count)





