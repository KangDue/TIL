import sys
sys.stdin = open('input.txt')

from collections import deque,defaultdict as df
d,w,r=int,input,range
for t in r(d(w())):
    n=d(w())
    maze=['1'*(n+2)]+['1'+w()+'1' for i in r(n)]+['1'*(n+2)]
    for y in r(n+2):
        x=maze[y].find('2')
        z=maze[y].find('3')
        if x > -1:s=[y,x,0]#출발지 찾기
        if z > -1:e=(y,z)  # 출발지 찾기
    q=deque([s])
    hist=df(d)
    di=[[1,0],[-1,0],[0,1],[0,-1]]
    while len(q):
        pos=q.popleft()
        for row,col in di:
            y,x=pos[0]+row,pos[1]+col
            if maze[y][x] != '1' and (y,x) not in hist:
                q.append([y,x,pos[2]+1])
                if hist[(y,x)]:
                    if hist[(y,x)] > pos[2]+1: hist[(y,x)]=pos[2]+1
                else: hist[(y,x)] = pos[2]+1
    if hist[e]:ans=hist[e]-1
    else:ans=0
    print(f'#{t+1} {ans}')





