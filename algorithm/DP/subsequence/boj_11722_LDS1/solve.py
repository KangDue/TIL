import sys
sys.stdin = open('input.txt')

import sys
ip = sys.stdin.readline
if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())
    nums = list(map(int,sys.stdin.readline().split()))
    dp = [[1,nums[i]] for i in range(n)]
    for i in range(1,n):
        mv = 1;c=0
        for j in range(i):
            if dp[j][1] > dp[i][1]: #앞에서 큰놈들만 고려, 최대값 갱신
                if mv < dp[j][0]:
                    mv = dp[j][0]
                c+=1
        if c:
            dp[i][0] = mv + 1
    print(max(dp)[0])