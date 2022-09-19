import sys
sys.stdin = open('input.txt')
"""
rgb거리에는 집이 n개 있다.
거리는 선분, 1~N번집 순서대로 존재
집은 R,G,B중 하나로 칠해야 한다.
각 색별 비용이 주어질때
- 각 집은 앞뒤로 색이 달라야 한다.
- 앞이나 뒤가 없다면 있는 곳만 비교
이때 모든 집 칠하는 비용의 최솟값
"""
# 방법 1. 답은 나오는데 시간초과 ㅎㅎ;
# 그럼 이 문제가 greedy 한가? 아니다!
# dp를 생각해보자
# import heapq
# I=lambda:int(input())
# n = I() #집 수
# q=[(-1,0,-1)]#step,비용,고른색 번호
# house = []
# for _ in range(n):
#     house.append([*map(int,input().split())])# 각 집별 칠하는 비용
# while q:
#     step,value,color = heapq.heappop(q)
#     if step == n-1:
#         print(value);break
#     for i in range(3):
#         if i != color:
#             heapq.heappush(q,[step+1,value+house[step+1][i],i])

# 방법 2. dp
I=lambda:int(input())
n = I() #집 수
dp = [[0,0,0] for _ in range(n+1)]
for i in range(1,n+1): #각 선택지별 점화식
    r,g,b = map(int,input().split())# 각 집별 칠하는 비용
    dp[i][0] = r+min(dp[i-1][1],dp[i-1][2])
    dp[i][1] = g+min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = b+min(dp[i - 1][0], dp[i - 1][1])
print(min(dp[n]))
