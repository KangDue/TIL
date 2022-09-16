import sys
# sys.stdin = open('input.txt')
"""
비어있는 공집합 S가 주어졌을 때
add (추가, 있다면 무시)
remove (제거, 없다면 무시)
check 있으면 1, 없으면 0 출력
toggle x 있으면 제거 없으면 추가
all S를 1~20 집합으로 변경
empty 공집합으로 변경
굳이 형변환 안함.
open으로 한번에 땡겨와도 그 양이 너무 많아서 메모리 초과뜸
open 하고 next 하는거 자체가 이미 open 으로 메모리를 잡아먹음
??? 이게 문제가 아니었나보다 . sys.stdin.readline 써도 메모리 초과뜸
dict 말고 list 써보자... 결국 안됨 문제는 pypy
메모리가 제한이 많이 걸린다면 python3를 활용하자.
같은 코드인데 python3 는 됨.
"""
import sys
input = sys.stdin.readline
n=int(input())
info = [0]*21
for i in range(n):
    order = input().split()
    if len(order) == 2:
        t = int(order[1])
        if info[t]: #여부 확인.
            if order[0] == 'remove' or order[0] == 'toggle':
                info[t] = 0
            elif order[0] == 'check':
                print(1)
        else:
            if order[0] == 'add' or order[0] == 'toggle':
                info[t]=1
            elif order[0] == 'check':
                print(0)
    else:
        if order[0] == 'all':
            info = [1]*21
        else:
            info = [0]*21
## open + dict 조합이 젤 빠름.
## open + list 조합 속도를 보자 list보단 dict가 조금 더 빠르다.
# o = open('input.txt'); n=int(next(o))
# info = [0]*21
# while 1:
#     try:
#         order = next(o).split()
#         if len(order) == 2:
#             t = int(order[1])
#             if info[t]:  # 여부 확인.
#                 if order[0] == 'remove' or order[0] == 'toggle':
#                     info[t] = 0
#                 elif order[0] == 'check':
#                     print(1)
#             else:
#                 if order[0] == 'add' or order[0] == 'toggle':
#                     info[t] = 1
#                 elif order[0] == 'check':
#                     print(0)
#         else:
#             if order[0] == 'all':
#                 info = [1] * 21
#             else:
#                 info = [0] * 21
#     except: break