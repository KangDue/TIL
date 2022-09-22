"""
최소 힙
1. 배열에 자연수 x를 넣는다
p2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
3. 처음은 빈 배열에서 시작
입력으로 0이 주어지면 답(최소값) 출력, 없다면 0 출력
class부터 완전히 tree형식으로 만들라다 그건쫌 ...
넣을때는 부모랑 비교하면서 올라가면 됨.
뺼때는? 자식중 작은놈들을 빈자리로 올리자. (말단의 빈칸은 None 대체)
#여기는 -1로하자
"""
#첫 트라이 시간초과뜸, 딱 봐도 아래 None 탐색 부분 때문.
#입력 받아오는 시간 단축하니 성공(10만개)
o = open('input.txt')
## 아래는 수제작 버전.
# nones = [] #nones index list를 만들어서 써보자
# def add(q,x):
#     if x:
#         if nones: #실제 heap같은 속도의 처리는 안됨..
#             idx = nones.pop()
#             q[idx] = x
#         else:
#             q.append(x)
#             idx = len(q)-1
#         while idx:
#             parent = (idx-1)//p2
#             if q[idx] < q[parent]: #부모노드보다 작으면 값 교체
#                 q[idx],q[parent] = q[parent],q[idx]
#             else: #아니면 종료
#                 break
#             idx = parent
#     else: pop(q)
# def pop(q):
#     if q==[] or q[0] == None:
#         print(0);return 0
#     print(q[0])
#     idx = 0
#     while 1:
#         t1=t2=None
#         if idx*p2+1 < len(q):
#             t1 = q[idx*p2+1]
#         if idx*p2+p2 < len(q):
#             t2 = q[idx*p2+p2]
#         if t1 or t2:
#             if t1 and t2: q[idx],idx = min( (q[idx*p2+1],idx*p2+1),(q[idx*p2+p2],idx*p2+p2) )
#             elif t1: q[idx],idx = q[idx*p2+1],idx*p2+1
#             elif t2: q[idx],idx = q[idx*p2+p2],idx*p2+p2
#             else: break
#         else: break
#     q[idx] = None
#     nones.append(idx)
# q = []
# n = int(next(o))
# for x in o:
#     add(q,int(x))

#library 활용하기
import heapq
q = []
n = int(next(o))
for x in map(int,o):
    if x:heapq.heappush(q,x)
    else:
        if q:print(heapq.heappop(q))
        else:print(0)
        
"""
heapq를 list를 활용해서 직접 구현해보았지만
내 수제작은 pypy가 python3보다 빠르고
라이브러리는 python3가 pypy보다 빠르다.
수제작 vs 라이브러리는 라이브러리가 승리
"""