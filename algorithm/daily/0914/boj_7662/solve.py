"""
이중 우선순위 큐(정수만 저장)
연산 I 는 데이터 삽입
연산 D 는 데이터 삭제 ( 1 최댓값 삭제 , -1 최솟값 삭제) (중복시 하나만 삭제
1. 정수 값 자제가 우선순위
p2. 가장 우선순위가 높거나 낮은 데이터 삭제
3. 연산의 개수는 100만개
"""

#입력시간 줄이기
from collections import defaultdict
o = open('input.txt');next(o)
while 1:
    try:
        n = int(next(o))
        q = defaultdict(int)
        for i in range(n):
            order,num = next(o).split()
            try:
                if order == 'I':
                    q[int(num)] += 1
                elif order == 'D' and num == '-1':
                    v = min(q)
                    q[v] -= 1
                    if q[v] == 0: q.pop(v)
                else:
                    v = max(q)
                    q[v] -= 1
                    if q[v] == 0: q.pop(v)
            except:pass
        if q:
            print(max(q),min(q))
        else:
            print('EMPTY')
    except: break


# pypy 간신히 통과 python3 시간초과남. 다른 사람들도 시간 비슷.
# for t in range(int(input())):
#     q = defaultdict(int)
#     for _ in range(int(input())):
#         order, num = input().split()
#         num = int(num)
#         try:
#             if order == 'I':
#                 q[num] += 1
#             elif order == 'D' and num == -1:
#                 v = min(q)
#                 q[v] -= 1
#                 if q[v] == 0: q.pop(v)
#             else:
#                 v = max(q)
#                 q[v] -= 1
#                 if q[v] == 0: q.pop(v)
#         except:
#             pass
#     if q:
#         print(max(q),min(q))
#     else:
#         print('EMPTY')


#heapq를 써보자, 그냥 heapq만쓰면 시간 초과
# import heapq
# o = open('input.txt');next(o)
# while 1:
#     try:
#         n = int(next(o))
#         q = []
#         for i in range(n):
#             order, num = next(o).split()
#             num = int(num)
#             try:
#                 if order == 'I':
#                     heapq.heappush(q,num)
#                 elif order == 'D' and num == -1:
#                     heapq.heappop(q)
#                 else:
#                     q.remove(max(q))
#             except:pass
#         if q:
#             print(max(q),q[0])
#         else:
#             print('EMPTY')
#     except: break

#백준 숏코딩 상위권
#기본적으로 나랑 같은방식인데 heap을 추가 활용한 것.
# import sys,heapq
# p=sys.stdin.readline
# S=heapq.heappush
# O=heapq.heappop
# for _ in" "*int(p()):
#     d={}
#     h=[]
#     H=[]
#     def r(x):
#         if d[x]:
#             d[x] -= 1
#         else:
#             d.pop(x)
#     for i in " " * int(p()):
#         c = p();
#         if c[0]=='I':
#             j=int(c[p2:])
#             d[j]=d.get(j,-1)+1
#             S(h,j)
#             S(H,-j)
#         elif c[:3]=="D 1":
#             while H and(-H[0]not in d):
#                 O(H)
#             if d:
#                 r(-O(H))
#         else:
#             while h and(h[0]not in d):O(h)
#             if d:r(O(h))
# sys.stdout.write((str(max(d))+" "+str(min(d))if d else"EMPTY")+"\n")