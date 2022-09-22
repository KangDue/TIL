import sys
sys.stdin = open('input.txt')

"""
사탕게임
1. 처음 가장긴 녀석값을 찾는다.
p2. 색이 다른놈들 서로 바꾼다.
3. 바꿧을때 길이만 비교한다.
"""
def rcheck(i):#행에서
    t1 = 1
    maxv=1
    for x in range(1,n):
        if text[i][x] == text[i][x-1]: t1 += 1
        else: maxv = max(t1,maxv); t1 = 1
    return max(t1,maxv)

def ccheck(i):#열에서
    t2 = 1
    maxv = 1
    for y in range(1,n):
        if text[y][i] == text[y-1][i]:t2 += 1
        else: maxv = max(t2,maxv); t2 = 1
    return max(t2,maxv)

n=int(input())
text = [[*input()] for i in range(n)]

maxv=1
for i in range(n):#초기상태 체크
    maxv = max(maxv,rcheck(i),ccheck(i))
for i in range(n):
    for j in range(n-1):
        if text[i][j] != text[i][j+1]: #행방향 변경
            text[i][j], text[i][j+1] =  text[i][j+1], text[i][j] # 바꾸기
            maxv = max(maxv, rcheck(i), ccheck(j), ccheck(j+1))
            text[i][j], text[i][j+1] =  text[i][j+1], text[i][j] # 원상복귀
for i in range(n-1):
    for j in range(n):
        if text[i][j] != text[i+1][j]: #열방향변경
            text[i][j], text[i+1][j] =  text[i+1][j], text[i][j] # 바꾸기
            maxv = max(maxv, rcheck(i), rcheck(i+1), ccheck(j))
            text[i][j], text[i+1][j] =  text[i+1][j], text[i][j] # 원상복귀
print(maxv)

## 압도적 숏코딩.
# n=int(input())
# b=eval('[*input(),0]+'*n+'[0]*n')
# i=r=0
# f=lambda w,p=0:_!=0!=b[i+d]==b[i+{0:d,d:0}.get(p,p)]and-~f(w,p+w)
# for _ in b:
#  for d in-1,1,~n,-~n:r=max(r,f(1)+f(-1)-1,f(~n)+f(-~n)-1)
#  i+=1
# print(r)











