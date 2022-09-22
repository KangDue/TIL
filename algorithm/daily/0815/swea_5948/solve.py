import sys
sys.stdin = open('input.txt', encoding='utf-8')
from itertools import combinations as cb
a = []
#정수 7개중 3개를 골라 5번째로 큰 수 출력(중복 허용 x)
for t in range(int(input())):
    nums = list(map(int,input().split())) #내림차순 정렬
    push = {}
    com = cb(nums,3)
    while 1:
        try:
            push[ sum( next(com) ) ] = 1
        except:
            break
    rank = sorted(list(push.keys()))
    a.append(f'#{t+1} {rank[-5]}')
print(*a,sep='\n')


# for t in range(int(input())):
#     nums = sorted(list(map(int,input().split())),reverse=True) #내림차순 정렬
#     push = 0 # 상위 등수 고정.
#     rank = []
#     for i in range(6): #뭔 가 엄청난 규칙이 있을듯 한데 잘 안나오넹 ...
#         for j in range(i+1,7):
#             pivot = nums[i] - nums[j]
#             nf = True
#             for k in nums[j+1:]:
#                 rank.append(nums[i] + nums[j] + k)
#                 if k > pivot: #기준 이상은 카운트
#                     push += 1
#                     nf = False
#                 else: # 없으면 루프 끝
#                     break
#             if nf: # 기준 이상인 놈 못 찾으면 끝.
#                 break
#         if nf:
#             break
#     com = cb(nums,3)
#     push = push-p2 if push < 5 else 0
#     for i in range(5-push):
#         aa = next(com)
#     a.append(f'#{t+1} {sum(aa)}')
# print(*a,sep='\n')
