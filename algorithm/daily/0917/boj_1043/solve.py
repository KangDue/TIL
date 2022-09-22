import sys
sys.stdin = open('input.txt')
"""
거짓말: 지민이는 허언증이 있다.
몇몇은 진실을 알고 진실을 아는사람이 있으면 진실밖에 못말한다.
사람수 N, 진실을 아는 사람 주어지고
각 파티원들 번호 주어짐
지민이가 거짓말쟁이인거 안들키고 허언할 수 있는 파티개수 최대값
단순히 진실아는놈만 피하면 되는데 아니라
거짓말을 들은사람과 진실 아는놈이 만나는것도 안됨.
진실말할때 같이있던놈들은 하나도 겹치면 안됨.

어떤 방식으로 찾든 한그룹으로 묶는 방법은 일단 각 그룹별로 한번씩 묶고나서
각 그룹 vs 다른 모든그룹 각각 다 확인하고 나서야 포함관계가 완성이 됨.

#아래 예시에서 5는 1과 그룹으로 묶이는데 4는 부모가 바뀌지만 업데이트가 안됨.
#그래서 한 번 다시 훑어 줘야한다.
# 5 3
# 1 1
# 3 3 p2 1
# p2 4 5
# p2 5 1
"""

# 1. 유니온  파인드 방법
# n,m = map(int,input().split())
# a,*known = map(int,input().split())#진실 아는 사람 숫자와 그 번호
# c=m
# relation = [i for i in range(51)]
# sk = set(known)
# for i in known:
#     relation[i] = known[0]
#
# def find(x):
#     if relation[x]!=x:
#         relation[x]=find(relation[x])
#     return relation[x]
# def union(x,y):
#     x = find(x)
#     y = find(y)
#     if x == y: return 0
#
#     if x == known[0]:
#         relation[y] = x
#     elif y == known[0]:
#         relation[x] = y
#     elif x < y:
#         relation[y] = x
#     else:
#         relation[x] = y
#
# if a:
#     party = []
#     c = m
#     for _ in range(m):
#         b,*people = map(int,input().split())
#         party.append(people)
#         if b==1: # 1개일때 재껴버리는게 문제라서 이렇게 따로 잡아줘야함.
#             relation[people[0]] = find(people[0])
#         else:
#             for i in range(b-1):
#                 union(people[i],people[i-1])
#     for i in party: #? 쓸데없어보이는데 지워보자 = 쓸데없지 않음.
#         for j in i:
#             relation[j]=find(j)
#     for i in party:
#         for j in i:
#             if relation[j]==known[0]:
#                 c-=1
#                 break
#     print(c)
# else:
#     print(m)


# #방법 p2. set으로 직접 목격자 집합 만들기
# n,m = map(int,input().split())
# a,*known = input().split()#진실 아는 사람 숫자와 그 번호
# sk = set(known)
# T = [1]*m
# if a:
#     party = []
#     c = m
#     for _ in range(m):
#         b, *people = input().split()
#         sp = set(people)
#         party.append(sp)
#         temp = sk & sp
#         if temp: sk|=sp
#     for i in range(m): #교차로 업데이트 해줘야함.
#         for j in range(m):
#             temp = sk&party[j]
#             if temp: sk|=party[j];T[j]=0
#     print(sum(T))
# else:
#     print(m)

#방법 3. bfs 써보기
from collections import deque
I = lambda : map(int,input().split())
n,m = I()
a,*known = I() #진실 아는 사람 숫자와 그 번호
graph = [[] for i in range(51)]
for i in range(1,a): # 1번 진실을 아는자를 중심으로 그래프 생성
    graph[known[i]].append(known[0])
    graph[known[0]].append(known[i])
if a:
    head = []#파티별 한 놈씩 받아오기
    for _ in range(m):# 파티별로 그래프 연결
        b, *people = I()
        head.append(people[0])
        for i in range(b-1):
            for j in range(i+1,b):
                graph[people[i]].append(people[j])
                graph[people[j]].append(people[i])
    for i in head:
        if i == known[0]: m-=1
        else:
            visited = [0]*51
            q = deque([i])
            visited[i] = 1
            while q:
                try:
                    v = q.popleft()
                    for x in graph[v]:
                        if not visited[x]:
                            if x == known[0]: m-=1;raise Exception
                            q.append(x)
                            visited[x]=1
                except: break
    print(m)
else:
    print(m)