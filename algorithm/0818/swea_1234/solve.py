import sys
sys.stdin = open('input.txt',encoding='utf-8')

for t in range(1,11):
    n, nums = input().split()
    n = int(n)
    nums = list(nums)
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            del nums[i] #삭제하면 길이가 줄어드니까 똑같이 한번더
            del nums[i]
            i = 0 #삭제되면 i=0으로 초기화
            continue
        else:
            i += 1
    print(f"#{t} {''.join(nums)}")