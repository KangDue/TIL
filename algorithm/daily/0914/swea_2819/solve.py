import sys
sys.stdin = open('input.txt')
"""
격자판의 숫자 이어붙이기
4×4 크기의 격자판, 격자칸 숫자 0 ~ 9
격자판의 임의의 위치에서 시작해서, 동서남북 
네 방향으로 인접한 격자로 총 여섯 번 이동하면서, 
각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리수
만들 수 있는 서로 다른 일곱 자리 수들의 개수
4x4에서 못가는칸은 없다.
"""
from collections import deque
for t in range(int(input())):
    grid = [input().split() for _ in range(4)]
    to = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited = dict()
    for i in range(4):
        for j in range(4):
            q = deque([[i,j,'']])
            while q:
                y,x,num = q.popleft()
                if len(num) == 7:
                    visited[num]=1;continue
                for dy,dx in to:
                    ny = y+dy; nx = x + dx
                    if 0<= ny < 4 and 0<= nx < 4:
                        temp = num+grid[ny][nx]
                        if visited.get(temp):continue
                        q.append([ny,nx,num+grid[ny][nx]])
    print(f'#{t+1} {len(visited)}')