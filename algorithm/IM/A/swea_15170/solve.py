import sys
sys.stdin = open('input.txt')

d,w,r,l=int,input,range,list
"""
낚시터가 1~n까지 일렬로 늘어서 있다.
각 출입구에는 대기하는 낚시꾼들이 있다.
1. 하나의 출입구씩 선택해서 순차적으로 입장가능
2. 출입구에서 대기하는 낚시꾼들은 자신의 위치에서 가장 가까운 빈 낚시터로 이동, 차례대로 자리잡기
3. 바로 앞은 1m 좌우로 1칸씩은 추가로 1m 씩
4. 해당 출입구의 맨 마지막 사람은. 가장 가까운 빈자리가 2곳이면 하나 선택
    (마지막이 아니면 어딜 골라도 결과가 같음
5. 해당 출입구 낚시꾼들 자리잡기 끝나면 다른 출입구를 선택 위 과정 반복
6. 모두 자리를 잡기까지 이동거리의 합의 최소값.
- 무조건 가장 가까운곳 부터 가는점 유의
- 자리 못잡는 경우는 없음.
"""
def put(a,):
    start = 1 #바로앞이면 1m
    x,y = a
    a=b= x
    while seat[a]:a+=1
    while seat[b]:b-=1
    if abs(a-x) > abs(b-x):



d,w,r=int,input,range
for t in r(d(w())):
    n = d(w())
    pp = []
    for i in r(3):
        x,y = map(d,w().split()) #게이트 번호, 사람수
        pp.append([x,y])
    seat = [0]*(n+1)


