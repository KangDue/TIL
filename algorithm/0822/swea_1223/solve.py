import sys
sys.stdin = open('input.txt')

#압축버젼
w,d=input,int
for t in range(10):
    n,ex=w(),w()
    ip={'+':1,'*':2}
    op=[]
    a=''
    for i in ex:#식 전환
        if i.isdigit():
            a += i
        else:
            while op and ip[op[-1]]>=ip[i]:
                a+=op.pop()
            op.append(i)
    while op:
        a+=op.pop()
    s=[] #계산
    for i in a:
        if i.isdigit():
            s.append(i)
        else:#연산자를 만나면 2개를 뽑아서 계산
            b,a=s.pop(),s.pop() #먼저 뽑은게 뒤로감
            r=d(a)*d(b) if i=='*' else d(a)+d(b)
            s.append(f'{r}')
    print(f'#{t+1} {s[-1]}')


