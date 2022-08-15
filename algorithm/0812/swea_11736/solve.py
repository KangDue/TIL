import sys
sys.stdin = open('input.txt',encoding='utf-8')

T = int(input())

#1~N 인 N의 순열
for t in range(1,T+1):
#순열을 직접 만들 줄 알았으나 아니네..
    n = int(input())
    p = list(map(int,input().split()))
    #연속된 숫자 3개중 최소도 최대도 아닌 값
    count = 0
    for i in range(1,len(p)-1):
        if (p[i]-p[i-1])*(p[i]-p[i+1]) < 0:
            count += 1
    print(f'#{t} {count}')


