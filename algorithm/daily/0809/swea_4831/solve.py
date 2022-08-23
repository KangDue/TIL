import sys
sys.stdin = open('input.txt')
# 수정한 버전
# 전기버스 종점까지 최소 충전수
T = int(input())
for t in range(1,T+1):
    k,n,m = map(int,input().split())
    # 한번충전 이동가능 정류장 수, 0~n번 정류장, 충전 정류장
    supply = list(map(int,input().split()))
    temp = ""
    for i in range(n+1):
        if i in supply:
            temp += "1"
        else:
            temp += "0"
    count = 0
    where = k #마지막 충전 후 갈 step
    while where >= n:
        if len(temp)-1 <=k: #한번이면 간다.
            break
        else:
            idx = temp[1:k+1].rfind("1")+1 #출발 제외했으니 +1
            if idx > -1:#한 번 가는 거리안에 충전소 유무
                temp = temp[idx::]
                count += 1
                where += idx
            else:
                break
    if where >= n:
        print(f'#{t} {count}')
    else:
        print(f'#{t} {0}')