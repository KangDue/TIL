import sys
sys.stdin = open('input.txt')
"""
적록색약(초록,빨강 구분 안됌)
입력 matrix에 R,G,B중하나가 있을 수 있다.
한 구역은 같은 색으로 이루어져 있다.
적록색야이 아닌 사람이 본 구간 수
적록색약인 사람이 본 구간 수

How?
1. 기본적으로 앞선 유기농배추나 그림등 구역 구분 문제가 틀이다.
p2. 정말로 2가지 case를 따로 구분해도 상관 없으나 한번에 하는게 편하고 효율적이지 않겠나?
3. 적,록을 묶어서 하고 ... 생각이 잘 안나네 - 이거는 알아보면 좋을 듯
4. 적록을 하나로 볼때랑 따로볼때 2가지 case로 해주는게 좋겠다... ㅎ;
"""
from collections import deque
import copy
n = int(input())
cmap = [[*input()] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
cmap2 = copy.deepcopy(cmap) #2차원 배열 복사시에는 deepcopy써줘야 값 연동 안일어남
for i in range(n):#적록합치기
    for j in range(n):
        if cmap2[i][j] == 'G':
            cmap2[i][j] = 'R'
#deepcopy아니면 list comprehension 써줘야함.
visited2 = [[0 for _ in range(n)] for _ in range(n)]
to = [[1,0],[-1,0],[0,-1],[0,1]]
def check(i,j,cmap,visited,find):#find로 이뤄진 영역 체크
    q = deque([[i,j]])#자꾸 좌표 [[ ]]로 감싸는거 깜빡
    visited[i][j] = 1
    while q:
        y,x = q.popleft()
        for dy,dx in to:
            ny = y+dy; nx = x+dx
            if 0<=ny<n and 0<=nx<n and visited[ny][nx] == 0 and cmap[ny][nx] == find:
                q.append([ny,nx])
                visited[ny][nx] = 1

ans1,ans2 = 0,0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            check(i, j, cmap, visited, find=cmap[i][j])
            ans1 += 1
        if visited2[i][j] == 0:
            check(i, j, cmap2, visited2, find=cmap2[i][j])
            ans2 += 1
print(ans1,ans2)


#재귀용 참고코드
# import sys;sys.setrecursionlimit(10000)
# def s(g,a,b,R):
#   if 0<=a<N and 0<=b<N and g[a][b]==R:
#       g[a][b]=''
#       s(g,a-1,b,R)#상
#       s(g,a,b-1,R)#좌
#       s(g,a+1,b,R)#하
#       s(g,a,b+1,R)#우
# N=int(input());t=range(N)
# A=[];B=[]
# for _ in t:
#   x=input()
#   A.append(list(x))
#   B.append(list(x.replace('G','R')))
# l=r=0
# for i in t:
#   for j in t:
#     if A[i][j]:s(A,i,j,A[i][j]);r+=1
#     if B[i][j]:s(B,i,j,B[i][j]);l+=1
# print(r,l)