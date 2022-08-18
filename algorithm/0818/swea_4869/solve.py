import sys
sys.stdin = open('input.txt',encoding='utf-8')

tb = [0,1,3] + [0]*28
for i in range(3,31):
    tb[i] = 2*tb[i-2] + tb[i-1]
#1개 추가하는 경우의수 1개 = tb[n-1]
#2개 추가하는 경우의수 2개 = tb[n-2]*2
#초기값 설정후 점화식
for t in range(1,int(input())+1):
    print(f'#{t} {tb[int(input())//10]}')