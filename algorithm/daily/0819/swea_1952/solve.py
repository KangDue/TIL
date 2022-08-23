import sys
sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    cost = list(map(int, input().split()))
    plan = list(map(int, input().split())) # plan에서 i-1이 dp에서 i값임.
    dp = [0] * 13 # 시작 값 0 패딩, dp와 plan의 idx가 다름을 유의
    for i in range(1, 13):#이전비용      #1일 비용            #전까지 비용 + 한달비용
        dp[i] = min(dp[i - 1] + plan[i - 1] * cost[0], dp[i - 1] + cost[1]) #1일 비용과, 1달 비용 비교
        if i >= 3: # 3달차부터,
            dp[i] = min(dp[i - 3] + cost[2], dp[i]) # 3달전 비용 + 3달비와 , 그냥 현재까지 비용 비교
    ans = min(dp[12], cost[3]) # 1년 비용과 비교
    print(f"#{t} {ans}")

# 1번째 달에서 최소값은 각 비용중 하나.
# 2번째 달에서 최소값은