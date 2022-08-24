import sys
sys.stdin = open('input.txt')

d,w,r=int,input,range
for t in r(d(w())):
    n,m=map(d,w().split())#피자 화덕, 피자
    c=[*map(d,w().split())]#치즈양
    c=[[c[i],i+1] for i in r(m)]#번호붙이기
    q=c[:n]
    qq=c[n:];qq.reverse()
    while 1:#1개만 남을때까지
        try:
            for i in r(n):
                q[i][0] //= 2
                if q[i][0] == 0:
                    if qq: q[i]=qq.pop()
                check = list(filter(lambda x:x[0],q))
                if len(check)==1:
                    print(f'#{t+1} {check[0][1]}')
                    raise Exception
        except:break