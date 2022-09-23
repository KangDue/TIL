import sys
sys.stdin = open('input.txt')
"""
스티커
2행 n열 스티커가 있다
스티커마다 점수가 있고
변을 공유하는 스티커는 하나를 땔때 따라서 훼손됨.
이 때 점수의 합이 최대가 되도록 스티커를 뜯을 때 값
"""
for t in range(int(input())):
    n = int(input())
    stick = [[*map(int,input().split())],[*map(int,input().split())] ]
    dp = [[0]*n,[0]*n]
    dp[0][0] = stick[0][0]
    dp[1][0] = stick[1][0]
    #각 열까지의 최대값을 dp로 활용
    #굳이 테이블로 저장 안하고 값 하나씩 바꿔가며 해도 가능.
    for i in range(1,n):
        dp[0][i] = max(stick[0][i]+dp[1][i-1], dp[0][i-1])
        dp[1][i] = max(stick[1][i]+dp[0][i-1], dp[1][i-1])
    print(max(dp[0][-1],dp[1][-1]))

    a=b=0
    #여기는 값 하니씩 돌리기 버전
    # a,b를 stack의 첫행에서 받아오고 1~n으로 하니 n=1일때 오류뜸
    # 수정해주자! a=b=0 시작, 0~n
    # 크기가 작아서 그런가 딸랑 30ms 빠름,
    for i in range(n):
        c = max(stick[0][i]+b, a)
        d = max(stick[1][i]+a, b)
        a,b = c,d
    print(max(c,d))
