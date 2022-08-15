import sys

sys.stdin = open('input.txt',encoding='utf-8')
T = int(input())
for t in range(1,T+1):
    D, L, N = map(int,input().split())
    # 공격의 데미지 D + D*n*L/100 = D + D*L/100*n
    # 등차수열의 합. n= 0부터 N번 때림. range(0,N)까지임. N 미포함.
    # N*D + D*L/200*N*(N-1)
    ans = N*D + D*L/200*N*(N-1)
    print(f"#{t} {int(ans)}")
#반복으로 풀어도 되지만, 간단한 수학적인 방법도 사용가능