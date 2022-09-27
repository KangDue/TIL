import sys
sys.stdin = open('input.txt')
"""
충전지 교환 방식의 전기버스 운행
정류장에는 교환기 존재, 충전지 마다 최대로 운행 가능한 정류장 수가 정해짐
정류장과 충전지에 대한 정보가 주어질 때, 목적지 도착까지 필요한 최소한의 교환 횟수는 ?
1번출발 n번 종점.
마지막 정류장은 배터리가 없다.
"""
def go(c=0,now=1):
    global minv,station
    if now + station[now] >= n:
        minv = min(minv,c)
        return 0
    for i in range(now+1,now+1+station[now]): #현재 위치에서 갈 수 있는 곳.
        if c < minv:
            go(c+1,i)


for t in range(int(input())):
    n,*station = map(int,input().split())
    station = [0] + station + [0]
    minv = len(station)
    go()
    print(f'#{t+1} {minv}')