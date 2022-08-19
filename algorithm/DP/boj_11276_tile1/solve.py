import sys
sys.stdin = open('input.txt')

import sys
#1x2 , 2x1 타일링, 2xn 채우기
if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())
    dp = [0,1,2] + [0]*(n-2) #초기값 설정 잘하고 위치계산 주의
    #N개가 이미 차있을때 1개를 추가하는 방법은 2x1 추가 1개
    #2개를 추가하는 방법은 (1x2)*2 하나, 2x1은 넣어봤자 위와 같은 경우
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    #문제 출력조건 잘보기 10007로 나눈 나머지 출력
    print(dp[n]%10007)

#dp라고 무조건 table을 만들 필요는 없다.
#점화식처럼해도 됨. (저장공간 절약, 시간 조금 절약)