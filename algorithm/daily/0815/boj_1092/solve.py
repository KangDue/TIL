import sys
sys.stdin = open('input.txt', encoding='utf-8')
# import sys
# ans =[]
# for t in range(1, int(sys.stdin.readline())+1):
#     n = int(sys.stdin.readline())
#     crains = sorted(list(map(int,sys.stdin.readline().split())))
#     m = int(sys.stdin.readline())
#     boxes = list(map(int,sys.stdin.readline().split()))
#     for i in range(n):
#         if crains[i] >= min(boxes):
#             n -= i  # 쓸수 있는 크레인 갯수
#             crains = crains[i:]  # 최소 무게도 못움직이는 crain 제외
#             break
#     nums = [0 for i in range(n)]
#     idx = 0
#     while boxes: # 크레인 무게별 자기만 옮길수 있는 녀석 갯수 체크
#         i = boxes.pop()
#         for k in range(n):
#             if i <= crains[k]:
#                 nums[k] += 1
#                 break
#     step = 0
#     length = n
#     for i in range(n-1):
#         if nums[i] % length and nums[i] > 0: #나머지가 있으면
#             nums[i+1] -= (nums[i]//length+1)*length
#             step += nums[i]//length + 1
#         elif nums[i] > 0: #0이하거나 나머지가 없다면 스텝 0 더하거나 스텝 바로 더하기
#             step += nums[i]//length
#         length -= 1
#     if nums[-1] > 0:
#         step += nums[-1]
#     ans.append(f'#{t} {step}') # 3배의 불필요한 연산이 발생하긴 하나 . 그냥 ㄱ
# print(*ans,sep = '\n')

# count = 0
# for i in range(m-2):
#     for j in range(i+1,m-1):
#         for k in range(j+1,m):
#             if len(list(set(info[i] + info[j] + info[k]))) == 3:
#                 count += 1

# while 1:
#     second += 1
#     print(nums)
#     for i in range(n-1,0,-1):
#         if nums[i]: # 0보다 클때만 -1
#             nums[i] -= power[i]
#         elif nums[i] == -1:
#             pass
#         else:
#             nums[i] = -1
#             power[i-1] += power[i]
#     if nums[0] > 0:
#         nums[0] -= power[0]
#
#     for i in nums:
#         if i > 0:
#             break
#     else: #전부 0보다 작으면 break
#         break

import sys
n = int(sys.stdin.readline())
crains = sorted(list(map(int,sys.stdin.readline().split())),reverse = True)
m = int(sys.stdin.readline())
boxes = sorted(list(map(int,sys.stdin.readline().split())), reverse = True)
if boxes[0] > crains[0]:
    step = -1
else:
    step = 0
    while boxes:
        for crain in crains:
            for box in boxes:
                if crain >= box:
                    boxes.remove(box)
                    break
        step += 1
print(f'{step}')