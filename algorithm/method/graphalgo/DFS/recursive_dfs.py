#### dfs 재귀 참고 (dfs는 재귀적 가능, bfs는 불가능)
#### 문제 채점현황보면 보통 재귀적으로 푼 코드가 더 빠른데
#### 큐에 넣고 빼고, while 조건문 비교하는 구간에서 속도차이가 나는듯 하다.
# 상하좌우 이동 설정
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# dfs 정의
def dfs(x, y):
    global cnt # cnt를 사용하기 위해 global 선언
    visited[x][y] = True
    if graph[x][y] == 1:
        cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False and graph[nx][ny] == 1:
                dfs(nx, ny)