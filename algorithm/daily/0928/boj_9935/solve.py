import sys
sys.stdin = open('input.txt')
"""
문자열 폭발!
문자열 A 와 B가 주어질때 A에서 B를 연쇄 폭발시키고 남은 문자열은?
없으면 'FRULA' 출력
최대길이 100만의 문자열, list로 만들면 너무 비효율 적일 가능성 있음.
find방법을 바꿔보았으나 48%에서 시간 초과 ...
string 만드는 방법도 바꿔보았으나 실패 ..
어떻게 binary하게 탐색할 방법이 있을까??
"""

# 시도 1 - 13프로까진가 하고 시간초과 떠버림 ㅋㅋ
# 시도 2 - find에 start argument를 넣을수 있길래 넣어봄, 빨라지긴함.
# 시도 3 - ans를 list로 받고 join함 더 빨라진거 같긴한데 47%의 벽을 못넘음
# def remake(arr):
#     ans = ''
#     for i in range(0,len(arr),2):
#         ans += A[arr[i]:arr[i+1]]
#     return ans
# A,B = input(),input()
# n = len(B)
# while 1:
#     la = len(A)
#     temp = [0]
#     idx = 0
#     for i in range(la):
#         pos = A.find(B,idx)
#         if pos > -1:
#             ans += A[arr[i]:arr[i+1]]
#             temp.append(pos)
#             temp.append(pos+n)
#         else:
#             break
#         idx = pos + n + 1
#     temp.append(la)
#     if len(temp) == 2: # 더 이상 없으면 끝
#         break
#     A = remake(temp)
# if A:
#     print(A)
# else:
#     print('FRULA')

#시도2 split and join 이것도 48% 찍고 좌절 ...
# A,B = input(),input()
# temp = A.split(B)
# A = ''.join(temp)
# while len(temp) > 1:
#     temp = A.split(B)
#     A = ''.join(temp)
# if A:
#     print(A)
# else:
#     print('FRULA')

#시도 3. 혹시나 싶은 마음에 안했던 방법인데 진짜 이게 더빠른게 맞누?
A,B = input(),[*input()]
lb = len(B)
stack = []
for i in A:
    stack.append(i)
    if stack[-1] == B[-1] and stack[-lb:] == B:
        for i in range(lb):
            stack.pop()
A = ''.join(stack)
if A:
    print(A)
else:
    print('FRULA')
