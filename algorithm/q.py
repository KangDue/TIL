def dfs(r,c):
    global visited, graph
    d = [[1, 0], [-1, 0], [0, -1], [0, 1]]  # 상하좌우
    if maze[r][c] == '3':# 종료 조건
        return 1
    elif maze[r][c] == '0':
        maze[r][c] = '1'
    for dd in d:
        r,c = v[0]+dd[0], v[1]+dd[1]
        if 0 <= r < n and  0 <= c < n:#유효범위
            if maze[r][c] != 1:
                dfs(r,c)
    return 0 # 갈수 있던 경로 전부 벽이 되면 0

