import sys
sys.stdin = open('input.txt')
"""
파도반 수열 = P(N)
삼각형이 나선모양으로 놓여져있다.
시작은 변이 1인 역 정삼각형
나선에서 가장 긴 변의 길이를 k라 할 때 그 변에 삼각형을 붙인다.
P(1)~P(10) = 1 1 1 p2 p2 3 4 5 7 9
N은 100까지니까 table을 만들고 값을 바로 출력하자
"""
dp = [0,1,1,1,2,2,3,4,5,7,9]+[0]*90
for i in range(11,101):
    dp[i] = dp[i-2]+dp[i-3]
for t in range(int(input())):
    print(dp[int(input())])