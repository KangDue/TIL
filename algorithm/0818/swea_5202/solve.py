import sys
sys.stdin = open('input.txt',encoding='utf-8')

for t in range(1,int(input()) +1 ):
    n = int(input())
    time = []
    for i in range(n):
        s, e = map(int,input().split())
        time.append((s,e))
    time.sort(key = lambda x:(x[1],x[0]))
    ans = [(0,0)]
    for i in range(0,n):
        if time[i][0] >= ans[-1][1]: # 다음 타임 시작이 앞 타임 종료시간 이상이면
            ans.append(time[i])
    print(f'#{t} {len(ans)-1}')