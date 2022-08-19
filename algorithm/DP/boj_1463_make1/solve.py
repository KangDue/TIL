import sys
sys.stdin = open('input.txt')

#3으로 나누기, 2로나누기, 1빼기로 가장 적은 연산으로 1 만들기
if __name__ == "__main__":
    import sys
    dp =[0,0,1,1] + [0]*(10**6-3)
    for i in range(4,10**6+1): #나눠 떨어지면 최솟값 선택
        if i % 2 == 0 and i % 3 == 0: #둘다 나눠떨어질때 고려를 해줘야함.
            dp[i] = min(dp[i // 2], dp[i // 3], dp[i - 1]) + 1
        elif i % 2 == 0:
            dp[i] = min(dp[i//2], dp[i-1], dp[i-2] + 1) + 1
        elif i % 3 == 0:
            dp[i] = min(dp[i//3], dp[i-1], dp[i-2] + 1 ) + 1
        else:# 안 나눠지면 걍 더하기 -1 -2를 통해 2배수 3배수 경우를 다 확인해줘야함.
            dp[i] = min(dp[i-1] + 1,dp[i-2] + 2, dp[i-3] + 3)
    n = int(sys.stdin.readline())
    print(dp[n])





