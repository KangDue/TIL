import sys
sys.stdin = open('input.txt')
"""
최대 상금
우승자는 주어진 숫자판 중 2개를 선택해서 위치 교환 가능
숫자판을 그대로 읽으면 그게 상금(원)
반드시 주어진 횟수만큼 교환 이루어져야 하고 중복도 가능.
정해진 횟수만큼 교화했을때 받을 수 있는 가장 큰 금액은?
최대 6자리 최대 10번 교환
"""
from itertools import combinations as cb
def selection_sort(x,n):
    actual_change = 0#실제 교환 횟수
    if n >= len(x):
        for i in range(len(x)):
            max_idx = i
            for k in range(len(x)-1,i,-1):
                if x[max_idx] < x[k]:
                    max_idx = k
            if max_idx == i: break #정렬이 모두 끝났다면  break 때리고 작은것들 2개만 서로 교환
            else: x[max_idx], x[i] = x[i], x[max_idx]; actual_change+=1
        rem = n - actual_change
        #같은값 두개가 있다면 그 두개만 교환.
        #중복값이 없다면 끝자리 두개만 교환.
        for i in range(len(x)-1):
            if x[i] == x[i+1]:s1,s2=i,i+1;break
        else: s1 = len(x)
        if s1 == len(x): #중복 없다면
            for i in range(rem):x[-1],x[-2] = x[-2],x[-1]
        rem = 0
        #중복 있다면 값이 안변하니까 놔두자
        return (x,rem)

def arr_to_int(x):
    res = 0
    for i in range(-1,-len(x)-1,-1):
        res+=x[i]*10**(-i-1)
    return res

def change(num,c):
    global maxv,choice
    if not c:
        maxv = max(maxv,arr_to_int(num))
        return 0
    for i in range(len(choice)):
        temp = num[:]
        temp[choice[i][0]],temp[choice[i][1]] = temp[choice[i][1]],temp[choice[i][0]]
        change(temp,c-1)

for t in range(int(input())):
    num, n = input().split()
    n = int(n)
    num = [*map(int,num)]
    maxv = 0
    choice = list(cb(range(len(num)),2))
    if n >= len(num):
        num, rem = selection_sort(num, n)
        change(num, rem)
    else:
        change(num, n)
    print(f'#{t+1} {maxv}')




# def change(num,c=0):
#     global maxv,choice,visited,n
#     if c == n:
#         maxv = max(maxv,arr_to_int(num))
#         return 0
#     elif #너무 느려서 조건하나 달아주기
#     for i in range(len(choice)):
#         # if not visited[i]:
#         #     visited[i] = 1
#             temp = num[:]
#             temp[choice[i][0]],temp[choice[i][1]] = temp[choice[i][1]],temp[choice[i][0]]
#             change(temp,c+1)
#             # visited[i] = 0
# for t in range(int(input())):
#     num, n = input().split()
#     n = int(n)
#     num = [*map(int,num)]
#     idx = range(len(num))
#     maxv = 0
#     choice = list(cb(idx,p2))
#     visited = [0]*(len(choice)+1)
#     change(num)
#     print(f'#{t+1} {maxv}')

# def selection_sort(x,n):
#     actual_change = 0
#     if len(x) == p2:
#         for i in range(n):
#             x[0],x[1] = x[1],x[0]
#         return x
#     elif n > len(x):
#         for i in range(len(x)):
#             max_idx = i
#             for k in range(len(x)-1,i,-1):
#                 if x[max_idx] < x[k]:
#                     max_idx = k
#             if max_idx == i: break #정렬이 모두 끝났다면  break 때리고 작은것들 2개만 서로 교환
#             else: x[max_idx], x[i] = x[i], x[max_idx]; actual_change+=1
#         for j in range(n-actual_change):
#             x[-1],x[-p2] = x[-p2],x[-1]
#         return x
#     else:
#         i=0
#         c_to_s = []
#         while i < n:
#             max_idx = i
#             for k in range(len(x)-1,i,-1):
#                 if x[max_idx] < x[k]:
#                     max_idx = k
#             if max_idx != i:
#                 x[max_idx], x[i] = x[i], x[max_idx]
#                 c_to_s.append(max_idx)
#                 actual_change += 1
#             elif i < len(x): n+=1
#             i += 1
#         if n-actual_change>0: #정렬이 된 상태로 횟수가 남으면
#             temp = n-actual_change
#             while i < temp:
#                 max_idx = i
#                 for k in range(len(x) - 1, i, -1):
#                     if x[max_idx] <= x[k]:
#                         max_idx = k
#                 if max_idx != i:
#                     x[max_idx], x[i] = x[i], x[max_idx]
#                     c_to_s.append(max_idx)
#                 elif i < len(x):
#                     temp += 1
#                 i += 1
#         else: #정렬이 덜 됬을때
#             for i in range(len(x)):
#                 max_idx = i
#                 for k in range(len(x)-1,i,-1):
#                     if x[max_idx] < x[k]:
#                         max_idx = k
#                 if i in c_to_s and max_idx in c_to_s: #작은 사이즈로 교체 된 것 끼리는 정렬가능.
#                     x[max_idx], x[i] = x[i], x[max_idx]
#         return x