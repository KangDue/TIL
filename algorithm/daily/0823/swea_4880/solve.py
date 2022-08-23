def whowin(x,y): #가위바위보 123
    info = {1:3, 2:1, 3:2}
    if info[x[0]] == y[0]:
        return x
    elif x[0] == y[0]:
        if x[1] < y[1]: #동점은 앞 번호 승
            return x
        else: return y
    else:
        return y

def to(x):
    if len(x) == 1:
        return x
    elif len(x) == 2:
        return [whowin(x[0],x[1])]
    else:
        return to( to(x[:(len(x)-1)//2+1]) + to(x[(len(x)-1)//2+1:]) )

for t in range(1,int(input())+1):
    n = int(input())
    st = list(map(int,input().split()))
    st = [ (st[i],i+1) for i in range(n)] #학생별 번호 부여
    ans =  to(st)[0][1]
    print(f'#{t} {ans}')