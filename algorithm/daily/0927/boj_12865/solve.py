import sys
sys.stdin = open('input.txt')
"""
01배낭
배낭의 들어갈 수 있는 가치의 합의 최댓값
"""
# n,k = map(int,input().split())
# loads = [[0,0]]
# for _ in range(n):
#     w,v=map(int, input().split())
#     loads.append((w,v))
# loads.sort(key = lambda x:x[0])
# dp = [[0]*(k+1) for _ in range(n+1)]
# for i in range(1,n+1):
#     for j in range(1,k+1):
#         w,v = loads[i]
#         if j<w: $dp의 j무게 일때가 w보다 작은 동안은 윗것만 가져옴
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)
# print(dp[-1][-1])

##
# 숏코딩 참고.
# n,k=map(int,input().split())
# d=[0]*(k+1)
# for _ in range(n):
#   w,v=map(int,input().split())
#   for i in range(k,w-1,-1):d[i]=max(d[i-w]+v,d[i])
# print(d[k])

#참고해서 만든 코드
n,k = map(int,input().split())
dp = [0]*(k+1)
for _ in range(n):
    w,v=map(int, input().split())
    for ele in range(k,w-1,-1):
        dp[ele] = max(dp[ele-w]+v,dp[ele])
print(dp[k])