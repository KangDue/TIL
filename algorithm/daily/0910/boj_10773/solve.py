import sys
a=open('input.txt')
a=open(0) # 이렇게 1줄씩 들어오는 입력 한번에 받을 수 있다.!!!
nums = [*map(lambda x: int(x.rstrip()),a)]
stack = []
ans = 0
for i in nums:
    if i: stack.append(i); ans += i
    else: ans -= stack.pop()
print(ans-nums[0])



# k = int(input())
# ans = 0
# stack = []
# for i in range(k):
#     temp = int(input())
#     if temp:
#         stack.append(temp)
#         ans += temp
#     else:
#         ans -= stack.pop()
# print(ans)