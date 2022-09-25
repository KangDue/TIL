import sys
sys.stdin = open('input.txt')
"""
전구와 스위치
스위치를 누르면 자기자신과 좌우 전구 상태 반전
"""
sw = {'1':'0','0':'1'}
def switch(i,A):
    for j in range(i-1,i+2):
        if 0<=j<n:
            A[j] = sw[A[j]]

n = int(input())
A=[*input()]
B=[*input()]
if A==B:
    print(0)
else:
    A_1 = A[:]
    switch(0,A_1)
    c_0 = 0 # 첫 스위치 안누르고 시작
    c_1 = 1 # 첫 스위치 누르고 시작
    for i in range(1,n):
        if A[i-1] != B[i-1]:
            switch(i,A)
            c_0+=1
    for i in range(1,n):
        if A_1[i-1] != B[i-1]:
            switch(i,A_1)
            c_1+=1
    candi = []
    if A==B:
        candi.append(c_0)
    if A_1 == B:
        candi.append(c_1)
    if candi:
        print(min(candi))
    else:
        print(-1)