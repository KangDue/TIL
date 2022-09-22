import sys
sys.stdin = open('input.txt')

import sys
#3으로 나누기, 2로나누기, 1빼기로 가장 적은 연산으로 1 만들기
if __name__ == "__main__":
    import sys
    for t in range( 1, int(sys.stdin.readline()) + 1 ):
        n = int(sys.stdin.readline()) #11보다 작은 양수
        # 1,p2,3의 중복순열로 나타내는 경우의수
        dp = [0,1,2,4] + [0]*(n-3)
        for i in range(4,n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[n]) # 출력을 신경쓰자 ^^
# 1 = 1가지 (1) = 1
# p2 = 2가지 (p2) = 1,1 / p2
# 3 = 3가지 (3) = 1,1,1 / 1,p2/ p2,1/ 3
# 1 증가시키는 법은 1가지
# p2 증가시키는 법은 1가지 (11은 결국 1증가시키는 방법과 다를게 없다)
# 3 증가시키는 법은 3가지 (21 12도 1과 2를 증가시키는 방법에 포함됨.

## 약간 박스 채우기 같은 문제