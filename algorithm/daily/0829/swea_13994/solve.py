import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    n = int(input())#노선수
    #시점,종점은 반드시 정차,
    #버스1은 모든 정류장 정차
    # 2는 A가 짝수일때 사이의 모든 짝수, 홀수일떄 모든 홀수
    # 3은 A가 짝수면 모든 4의 배수, A가 홀수면 3의배수면서 10의 배수가 아닌것
    # 최대 몇개의 노선이 같은 정류장에 정차하나 ?
    # 버스 번호는 최대 1000
    station = [0]*1001
    for _ in range(n):
        t,a,b = map(int,input().split()) #버스타입, 시점, 종점
        if t == 1:
            for i in range(a,b+1): station[i] += 1
        elif t == 2:
            for i in range(a,b,2): station[i] += 1
            station[b]+=1
        else:
            if a%2:
                for i in range(a,b):
                    if i%3==0 and i%10: station[i] += 1
            else:
                for i in range(a,b):
                    if i%4==0: station[i] += 1
            station[b]+=1
    print(f'#{tc+1} {max(station)}')
