import sys
# sys.stdin = open('input.txt')
"""
메모장에서 비번찾기!
저장된 주소 수 N (max 10만)
찾으려는 사이트 수 (max 10만)
N M
사이트 비번
.
.
. (M개)
"""
o = open('input.txt')
n, m = map(int, next(o).split())
info = {}
c = 0
for i in range(n):
    x,y=next(o).split()
    info[x]=y
ans = []
for i in range(m):
    x=next(o).rstrip()
    ans.append(info[x])
print(*ans,sep='\n')