import sys
sys.stdin = open('input.txt')
#복 습 필 수!

# 계단오르기, 마지막은 반드시 밟아야 하고
# 연속 3칸 불가능
# 1칸 또는 2칸 뛰기 가능
if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())
    stairs = [0] + [int(sys.stdin.readline()) for i in range(n)]#시작점 0 padding
    idx = [0]
    dp = [0]*(n+1)
    dp[1] = 10
    dp[2] = 30
    for i in range(3,n+1):#자기 자신(마지막 계단) 밝음, or not
        dp[i] += max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
    print(dp[-1])