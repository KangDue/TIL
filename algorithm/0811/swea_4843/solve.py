import sys
sys.stdin = open('input.txt')
#색다른 정렬
#max1,min1,max2,min2 ... 정렬
#정렬 결과는 10개까지만 출력
T = int(input())
for t in range(1,T+1):
    n = int(input())
    nums = list(map(int,input().split()))
    mode = True
    for i in range(10): # 10개 까지만 정렬
        for k in range(-1,-n+i,-1):
            if mode:#max가져다 놓기
                if nums[k] > nums[k-1]:
                    nums[k] ,nums[k-1] = nums[k-1],nums[k]
            else:#min 가져다 놓기
                if nums[k] < nums[k-1]:
                    nums[k] ,nums[k-1] = nums[k-1],nums[k]
        mode = False if mode else True
    print(f'#{t} {str(nums[:10])[1:-1].replace(",","")}')