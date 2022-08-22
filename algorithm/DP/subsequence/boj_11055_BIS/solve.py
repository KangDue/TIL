import sys
sys.stdin = open('input.txt')

import sys
ip = sys.stdin.readline
if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())
    nums = list(map(int,sys.stdin.readline().split()))
    dp = [[nums[i],nums[i]] for i in range(n)] #증가 부분 수열중 합이 가장 큰것
    for i in range(1,n):
        mv = 0;c=0
        for j in range(i):
            if dp[j][1] < dp[i][1]: #증가 부분 수열 고려 중, 앞에서 작은놈들만 고려,최대값 갱신
                if mv < dp[j][0]:
                    mv = dp[j][0]
                c+=1
        if c:
            dp[i][0] += mv
    print(max(dp)[0])