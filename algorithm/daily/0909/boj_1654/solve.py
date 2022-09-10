import sys
sys.stdin = open('input.txt')
#같은 길이로 자른 lan선들이 필요하다.
#최대 길이는 lans중 최소길이. (K==N일수 있기때문)
#라고 생각했으나 이러면 최대 최소길이의 차이가 클때 반영이 안됨
# ex) 4 4, 40 40 40 5 일때 20으로 잘라도 6개가 만들어짐.
# 그러니까 max부터 찾자!
#여기서부터 1씩 감소하면서 찾아보자!
# min으로 했을때 잘린 갯수를 기준으로 가지치기하면
# 평균시간을 줄일수 있겠으나 걍 가자 ㅎ
# 바로 시간초과 뜨네 ...
# min값 기준으로 가자
# 얘는 왜 더 오래걸리지 이상하네 ..ㅠ
# 그러면 binary하게 찾아볼까???
k,n = map(int,input().split())
lans = []
for i in range(k):
    lans.append(int(input()))
ap = max(lans)
bp = 1
#몫기준으로 찾고 1씩 변화주기
maxv = ap//bp
while 1:
    ans = sum(map(lambda x:x//maxv,lans))
    if ans >= n:
        if bp == 1: break
        else:
            up = ap//(bp-1)
            down = maxv
            while up-down > 1:
                mid = (up+down)//2
                ans = sum(map(lambda x: x // mid, lans))
                if ans >= n:
                    down = mid
                else:
                    up = mid
            break
    else:
        bp += 1
        maxv = ap//bp
        # maxv = ap//bp 몫으로 하면 단위가 뛴다..


if bp == 1:
    print(maxv)
else:
    ans = sum(map(lambda x: x // up, lans))
    if ans >= n:
        print(up)
    else:
        print(down)





k,n,*a=map(int,open(0).read().split())
r=max(a)
l=m=1
while l<=r:
     m=(l+r)//2
     t=sum(x//m for x in a)
     if t<n:
         r=m-1
     else:
         l=m+1
         w=m
print(w)
