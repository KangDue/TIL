import sys
sys.stdin = open('input.txt')
"""
AC라는 정수 배열을 만들기 위한 언어가 있다.
R(뒤집기) D(버리기)라는 두가지 함수가 있다.
버리기는 첫번째 수를 버린다.
배열의 초기값과 수행할 함수가 주어질때
결과물을 출력하시오.
전체 테스트케이스에서 p길이와 n의 합은 70만 이하
배열의 정수는 양의정수 (0 미포함)
"""

for t in range(int(input())):
    funcs = input()
    n = int(input()) #배열 길이
    arr = input()[1:-1].split(',') #입력받아서 형변환하는 시간 많이 소요됨.
    idx,ridx = 0,-1                #값이 굳이 정수일 필요 없다면 변환할 필요 x
    rc,dc = funcs.count('R'),funcs.count('D')
    if dc > n: print('error')
    else:
        flag = 1
        for i in funcs:
            if i =='D' and flag: arr[idx] = 0; idx += 1
            elif i=='D': arr[ridx] = 0; ridx -= 1
            else: flag^=1
        ans=[]
        if flag:
            for i in range(n):
                if arr[i]: ans.append(arr[i])
        else:
            for i in range(n-1,-1,-1):
                if arr[i]: ans.append(arr[i])
        print('[',end='')
        print(*ans,sep=',',end='')
        print(']')

# from collections import deque
# for t in range(int(input())):
#     funcs = input()
#     n = int(input()) #배열 길이
#     arr = deque(eval(input()))
#     rc,dc = funcs.count('R'),funcs.count('D')
#     if dc > n: print('error')
#     else:
#         flag = True
#         for i in funcs:
#             if i =='D' and flag:
#                 arr.popleft()
#             elif i=='D': arr.pop()
#             else: flag = not flag
#         else:
#             arr = list(arr)
#             if rc%p2:arr.reverse()
#             print(str(arr).replace(" ",""))


