import sys
sys.stdin = open('input.txt')
"""
0~9 + - 로만 이뤄진 식에서
처음과 마지막은 항상 숫자여야하고
연속으로 두개이상 연산자가 등장하지 않고
5자리보다 큰 숫자는 없고 수는 0으로 시작 가능하고
식은 길이 50 이하이다.
이때 적절히 괄호를 쳐서 식의 결과룰 최소로 만드시오.
"""
# from operator import add,sub
# from itertools import combinations as cb
# from collections import deque
# text = input()+' '
# ex = []
# temp = ''
# oper = {'-':sub,'+':add}
# for i in text:
#     if i in '+-':
#         ex.extend([int(temp),oper[i]])
#         temp = ''
#     elif i == ' ':
#         ex.append(int(temp))
#     else:
#         temp += i
# def cal(s,e,ex):
#     result = ex[s]
#     for i in range(s,e,2):
#         result = ex[i+1](result,ex[i+2])
#     return result
# subidx = []
# for i in range(len(ex)):
#     if ex[i] == sub:
#         subidx.append(i)
# minv = sum(filter(lambda x:isinstance(x,int),ex))

"""재귀하니 시간초과...
값을 최소로 만들어야하니까 가지치기를 해보자!
양수끼리는 괄호 쳐봤자 의미가 있구나 ㅎㅎ;
"""
# def dfs(now):
#     global minv
#     if len(now) == 1:
#         if minv > now[0]: minv = now[0]
#     nums = range(0, len(now), 2)  # 숫자의 위치
#     for s,e in cb(nums,2):
#         if e == len(now) - 1:
#             result = now[:s]+[cal(s, e, now)]
#         else:
#             result = now[:s] + [cal(s, e, now)]+now[e+1:]
#         dfs(result)
# dfs(ex)
# print(minv)

"""반복문하니 메모리초과"""
# while q:
#     now = q.popleft()
#     nums = range(0, len(now), 2)  # 숫자의 위치
#     for s,e in cb(nums,2):
#         if e == len(now) - 1:
#             result = now[:s]+[cal(s, e, now)]
#         else:
#             result = now[:s] + [cal(s, e, now)]+now[e+1:]
#         if len(result) > 1:
#             q.append(result)
#         else:
#             if minv > result[0]: minv = result[0]

"""
greedy하게 보면 - 뒤의 숫자가 최대가 되어야 한다.
-뒤에서 부터 다음 -를 만나거나 끝날대 까지 걍 쭉 더하면 됨.
이렇게하니 pass!
"""
from operator import add,sub
text = input()+' '
ex = []
temp = ''
oper = {'-':sub,'+':add}
for i in text:
    if i in '+-':
        ex.extend([int(temp),oper[i]])
        temp = ''
    elif i == ' ':
        ex.append(int(temp))
    else:
        temp += i
def cal(s,e,ex):
    result = ex[s]
    for i in range(s,e,2):
        result = ex[i+1](result,ex[i+2])
    return result
subidx = []
for i in range(len(ex)):
    if ex[i] == sub:
        subidx.append(i)
nums = range(0, len(ex), 2)
if subidx: # -부호가 있을때, -부호 나오기 전까지 합
    result = cal(0,subidx[0]-1,ex)
    for i in range(len(subidx)):
        if i == len(subidx)-1: #뒤에 - 없다면 끝까지
            result -= cal(subidx[i]+1,nums[-1],ex)
        else:
            result -= cal(subidx[i]+1,subidx[i+1]-1,ex)
else:
    result = cal(0,nums[-1],ex)
print(result)

#아래는 지리는 숏코딩
#-로 분할한뒤 첫값은 항상 '' 또는 a + b - 꼴의 형태이니
#a로 시작값 하나 받고 나머지는 다 빼버리기.
a,*b=[sum(map(int,x.split("+")))for x in input().split("-")];print(a-sum(b))

