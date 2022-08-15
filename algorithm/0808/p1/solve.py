import sys
#당분간 sort sored 금지

sys.stdin = open('input.txt') #stdin을 하면 알아서 입력을 한 줄 씩 넣어준다.

T = int(input())
for t in range(1,T+1):
    n = int(input())
    nums = list(map(int,input().split()))
    l = len(nums)

    mv = nums[0] #제일 높은 곳
    for i in range(1,l):
        if mv < nums[i]:
            mv = nums[i]

    blocks = [[1 for i in range(mv)] for k in range(l)]#블록 지도
    for i in range(l):
        blocks[i][:nums[i]] = [0]*nums[i]

    ans = 0
    for i in zip(*blocks): # 옆으로 뒤집고 낙차 최대값 찾기
        if ans < sum(i[i.index(0):]): #낙차 카운트
            ans = sum(i[i.index(0):])
    print(f'#{t} {ans}')