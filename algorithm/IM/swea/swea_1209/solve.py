import sys
sys.stdin = open('input.txt')

d,w,r,l,s=int,input,range,list,sum
for t in r(10):
    w()#tc번호
    g = [l(map(d,w().split())) for k in r(100)]#원본
    d1 = s([g[i][i] for i in r(100)])#대각선 1
    d2 = s([g[i-1][-i] for i in r(1,101)])#대각선 p2
    row = [s(i) for i in l(zip(*g))]#Transpose
    print(f'#{t+1} {max([ s(i) for i in g]+row+[d1]+[d2])}')

