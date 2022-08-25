import sys
sys.stdin = open('input.txt')

d,w,r=int,input,range
def md(x,y):#두 점사이의 맨해튼 거리가 1보다 크면 다른 영역임
    return (abs(x[0]-y[0]) + abs(x[1]-y[1])) > 1
from functools import reduce
for t in r(d(w())):
    n = d(w())
    mat = [[0] + list(map(d,w().split())) + [0] for i in r(n)]
    mat = [[0]*(n+2)] + mat + [[0]*(n+2)] # zero padding
    #좌상단 모서리(좌,상) 우 하단 모서리(우,하)가 0이다.
    temp  = []
    for i in r(1,n+1):
        for j in r(1,n+1):
            if mat[i][j] and mat[i-1][j] == 0 and mat[i][j-1] == 0:#좌상단 꼭짓점 검출
                x=y=0 #sub matrix 행열 길이 검출
                while mat[i][j+x+1]:#열
                    x += 1
                while mat[i+y+1][j+x]:#행
                    y += 1
                temp.append([y+1,x+1])
    temp.sort(key=lambda x:(x[0]*x[1],x[0])) #크기순, 행길이순 오름차순 정렬
    length=len(temp)
    temp = reduce(lambda x,y:x+y,temp)
    print(f'#{t+1}',length,*temp)




    #print(f'#{t+1}',length,*result)

