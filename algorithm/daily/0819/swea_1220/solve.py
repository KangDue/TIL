import sys
sys.stdin = open('input.txt')

for t in range(1,11):
    n = int(input())
    nums = [list(map(int,input().split())) for i in range(n)]
    nums = list(zip(*nums)) #편하게 Transpose
    ans = 0
    for line in nums:
        stack = []
        for k in line:
            if not stack and k == 1:
                stack.append(k)
            if stack and k == 2:
                stack.pop()
                ans += 1
            else:
                pass

    print(f'#{t} {ans}')


