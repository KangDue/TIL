import sys
sys.stdin=open('input.txt')
for t in range(1,10+1):
    n = int(input())
    nums = list(map(int,input().split()))
    for i in range(100):
        for k in range(i,100):
            if nums[i] > nums[k]:
                nums[i] , nums[k] = nums[k], nums[i]

    while n > 0:
        try:
            a = -1 #위에서 빼기
            while 1:
                if nums[a] > nums[a-1]:
                    nums[a] -= 1
                    break
                a -= 1

            b = 0 # 아래에 쌓기
            while 1:
                if nums[b] < nums[b+1]:
                    nums[b] += 1
                    break
                b+=1
        except: #index 초과 = 조기종료
            break
        n -= 1

    ans = nums[-1]-nums[0]
    print(f'#{t} {ans}')