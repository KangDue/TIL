import sys
sys.stdin = open('input.txt')

def is_pal(x):
    if len(x) <= 1:return 1
    elif x[0] != x[-1]:return 0
    else:return is_pal(x[1:-1])
d,w,r=int,input,range
for t in r(10):#8x8글자판에서 길이가 n인 회문 찾기
    n=d(w())
    a=[w() for i in r(8)]
    b=[''.join(i) for i in zip(*a)]
    c=0
    for i in r(8):
        for j in r(9-n):
            if is_pal(a[i][j:j+n]):c+=1
            if is_pal(b[i][j:j+n]):c+=1
    print(f'#{t+1} {c}')
