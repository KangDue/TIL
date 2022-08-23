import sys
sys.stdin = open('input.txt')

def udlr_sum(i, k):
    global nums
    c = nums[i][k]
    u = abs(c - nums[i - 1][k])
    d = abs(c - nums[i - 1][k])
    l = abs(c - nums[i][k - 1])
    r = abs(c - nums[i][k + 1])
    return u + d + l + r

T =int(input())
for t in range(1,T+1):
    n = int(input())
    nums = [list(map(int,input().split())) for i in range(n)]
    #상하좌우 padding 넣기
    nums = [ [i[0]] + i + [i[-1]] for i in nums]
    nums = [nums[0]] + nums + [nums[-1]]

    #계산
    ans = 0
    for i in range(1,n+1):
        for k in range(1,n+1):
            ans += udlr_sum(i, k)
    print(f'#{t} {ans}')ㅔ

