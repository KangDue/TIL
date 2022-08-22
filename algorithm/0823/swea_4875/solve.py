# 미로 탈출 가능 불가능 ?
# 1은 벽, 2는 출발, 3은 도착, 0은 길
import sys
sys.stdin = open('input.txt')
for t in range(int(input())):
    n = int(input())
    maze = [input() for i in range(n)]
    s=e=0 #s = 2위치, e = 3위치
    for i in range(n-1,-1,-1):# 2찾기
        temp = maze[i].find('2')
        if temp > -1:
            s = [i,temp];break
    for i in range(n):#3찾기
        temp = maze[i].find('3')
        if temp > -1:
            e = [i,temp];break
    maze=[list(i) for i in maze]
    d = [[1,0], [-1,0], [0,-1], [0,1]]#상하좌우
    stack=[s]#출발점
    g = False # 도착시 True로 전환
    while stack:
        v = stack.pop()#뽑기
        maze[v[0]][v[1]] = 1 #지나간곳은 전부 벽으로 바꾸기
        for dd in d:#4방향 살피기
            r,c = v[0]+dd[0], v[1]+dd[1]
            if 0 <= r < n and  0 <= c < n:#유효범위
                if maze[r][c] == '3':
                    stack.append([r, c])
                    g = True;break
                elif maze[r][c] == '0':
                    stack.append([r, c])
            if g: break
        if g:print(f'#{t+1} 1');break
    else:
        print(f'#{t+1} 0')