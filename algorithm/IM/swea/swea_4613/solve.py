import sys
sys.stdin = open('input.txt')

from itertools import combinations as cb
d,w,r,c=int,input,range,str.count
for t in r(d(w())):
    info={'W':0,'B':0,'R':0}
    row,col=map(d,w().split()) # 행 열 길이 받아오기
    flag=[w() for i in r(row)]
    flag=[[c(i,'W'),c(i,'B'),c(i,'R')] for i in flag] #1 그냥 itertools 쓰자...
    #양끝은 하양,빨강이 먹고/ 중간영역에서 B가 차지하는 영역을 조합으로 나타내자
    minv=2500
    for c in cb(r(1,row),2):
        a,b = c
        temp = 0
        for i in r(a):#하얗게
            temp += flag[i][1]+flag[i][2]
        for i in r(a,b):#파랗게
            temp += flag[i][0] + flag[i][2]
        for i in r(b,row):#빨갛게
            temp += flag[i][0] + flag[i][1]
        if minv > temp:#최솟값
            minv = temp
    print(f'#{t+1} {minv}')

#짧게..
from itertools import combinations as cb
d,w,r,c=int,input,range,str.count
for t in r(d(w())):
    D={'W':0,'B':0,'R':0}
    q,p=map(d,w().split())
    f=[w() for i in r(q)];f=[[c(i,'W'),c(i,'B'),c(i,'R')] for i in f];mi=2500
    for _ in cb(r(1,q),2):
        a,b=_;tm=0
        for i in r(a):tm+=f[i][1]+f[i][2]
        for i in r(a,b):tm+=f[i][0]+f[i][2]
        for i in r(b,q):tm+=f[i][0]+f[i][1]
        if mi>tm:mi=tm
    print(f'#{t+1} {mi}')

