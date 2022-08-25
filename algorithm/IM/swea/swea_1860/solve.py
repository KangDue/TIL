import sys
sys.stdin = open('input.txt')
file = open('output.txt')
answers = []
for i in range(1000):
    answers.append(file.readline().strip())

#0~m초의 시간동안 k개 붕어빵 만듬
#예약손님 N명
#waiting 없이 손님들에게 붕어빵 제공이 가능한가?
d,w,r=int,input,range
for t in r(d(w())):
    n,m,k=map(d,w().split())
    pe = sorted([*map(d, w().split())])
    tb=[0]+[k]*(11111//m) #각 붕어빵 생산 구간별 개수 초기화, #개수가 남으면 넘어갈 수 있다.ㅎㅎ
    a=1
    tb[pe[0]//m]+=sum(tb[:pe[0]//m]) #첫 tb값 업데이트
    for i in r(len(pe)-1):
        e=pe[i]//m
        if tb[e]:tb[e]-=1
        else:a=0;break
        if e != pe[i+1]//m: #시간대 바뀌면 앞에거를 더해준다.
            tb[pe[i+1]//m]+=sum(tb[:e+1])
    else:
        if tb[pe[-1]//m]==0:a=0
    a='Possible' if a else 'Impossible'
    print(f'#{t+1} {a}')




