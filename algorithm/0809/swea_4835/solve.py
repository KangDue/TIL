import sys
sys.stdin = open('input.txt')

# 정수 n개 리스트중 연속된 m개의 합을 계산할때
# 가장 큰 경우와 작은 경우의 차이를 출력

T = int(input())
for t in range(1,T+1):
    n,m = map(int,input().split())
    nums = list(map(int,input().split()))
    maxv = -1
    minv = 10000*m

    for i in range(n-m+1):
        temp = 0
        for k in range(m):
            temp += nums[i+k]
        if maxv < temp:
            maxv = temp
        if minv > temp:
            minv = temp
    ans = maxv-minv
    print(f'#{t} {ans}')