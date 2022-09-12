import sys
# sys.stdin = open('input.txt')
# #듣도못한 사람, 보도못한사람 명단이 주어질 때 겹치는 사람 수
# n,m=map(int,input().split())
# nh={input() for i in range(n)}
# nd={input() for i in range(m)}
# ans=sorted([*nh&nd])
# print(len(ans),*ans,sep='\n')

#속도를 올려보자! 입력 최대 n+m 100만개
o=open('input.txt');next(o);info={}
for i in map(lambda x:x.rstrip(),o):
    if info.get(i)==0:info[i]+=1
    else:info[i]=0
l=sorted([*filter(lambda x:info[x],info)])
print(len(l),*l,sep='\n')
#이렇게하니 pypy는 시간차가 별로 안나지만
#python은 속도가 30배정도 빨라짐!

#숏코딩 파이썬 1위버전
n,m,*a=open(0).read().split()
n=int(n)
a=sorted({*a[:n]}&{*a[n:]})
print(len(a),*a)