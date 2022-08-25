import sys
sys.stdin = open('input.txt')

def is_pal(x):
    if len(x) <= 1:return 1
    elif x[0] != x[-1]:return 0
    else:return is_pal(x[1:-1])
def check():
    for n in r(100,0,-1): # 길이 점점 감소 시키기 (길이별로 전체 확인)
        for i in r(100):
            for j in r(101-n):
                if is_pal(a[i][j:j+n]):return n
                if is_pal(b[i][j:j+n]):return n
d,w,r=int,input,range
for t in r(10):#8x8글자판에서 길이가 n인 회문 찾기
    w()
    a=[w() for i in r(100)]
    b=[''.join(i) for i in zip(*a)]
    print(f'#{t+1} {check()}')