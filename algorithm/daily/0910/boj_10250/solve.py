import sys
sys.stdin = open('input.txt')
"""
호텔에서 손님들이 정문으로부터 거리가 가장 짧은 방을 선호
각 층에는 W개의 방, H 층 1 이상 99 이하
엘베는 가장 왼쪽
방번호 101 102 103 ~ 1층
이런 호텔을 H x W 호텔이라 한다.
호텔 정문은 1층 엘리베이터 바로앞에 위치.
방호수는 yxx 또는 yyxx (층,호수)
엘리베이터 타는 거리는 포함 안되는데 이걸 고려 실제거리에서 빼준값
기준으로 고객이 선호.-> 맨 앞 호실 부터 1열씩 채운다.
"""
for t in range(int(input())):
    H,W,N = map(int,input().split())
    a,b=divmod(N,H)
    a,b = (a+1,b) if b > 0 else (a,H)
    print(f'{b}{a:02}')









