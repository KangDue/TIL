import sys
sys.setrecursionlimit(100000)
sys.stdin = open('input.txt')
"""
D: n을 2배로 9999보다 커지면 나눈 나머지 값
S: n-1, 0이면 9999로
L: 자리수를 왼쪽으로 회전
R: R은 각 자리수를 오른편으로 회전
n은 0이상 10000미만
네 자릿수는 d1,d2,d3,d4 다.
서로다른 두 정수 A B에 대하여 
A를 B로 바꾸는 최소한의 명령어
"""

#1. 일단  최소 = 최단거리 느낌이라 큐로 접근
#맞추긴 하는데 바로 메모리초과 떠버린다... 어떻게 할까?
#아무리 생각해도 획기적인 방안이 ...
#메모리를 아끼기 위해 int대신 str그대로 써보자..는 파기 - 필요이상 연산 복잡해짐
# from collections import deque
# D = lambda x:(x*p2)%10000
# S = lambda x:(x-1)%10000
# def L(x):
#     x,y = divmod(x*10,10000)
#     return y+x
# def R(x):
#     x,y = divmod(x,10)
#     return y*1000+x
# funcs = dict(D=D,S=S,L=L,R=R)
# for t in range(int(input())):
#     A,B = map(int,input().split())
#     visited = [0]*10000
#     q = deque([[A,'']])
#     visited[A]=1
#     while q:
#         try:
#             v,hist = q.popleft()
#             for oper in funcs:
#                 nv = funcs[oper](v)
#                 if visited[nv]==0:
#                     visited[nv] = 1 #ㅋ 별 쑈를 다했는데 방문체크를 깜빡한거네 ㅋㅋㅋㅋㅋㅋㅋ
#                     q.append([nv,hist+oper]) #str덧셈말고 리스트로 바꿧는데 더 느려짐.
#                     if nv == B:
#                         print(hist+oper)
#                         raise Exception
#         except:break
#         #여기서 hist를 구하는 연산이 오래걸림
#         #hist 구하는 연산을 따로 백트래킹 방식으로 때어내면 시간 단축 가능

#Let's do it!
# from collections import deque
# D = lambda x:(x*p2)%10000
# S = lambda x:(x-1)%10000
# def L(x):
#     x,y = divmod(x*10,10000)
#     return y+x
# def R(x):
#     x,y = divmod(x,10)
#     return y*1000+x
# funcs = dict(D=D,S=S,L=L,R=R)
# for t in range(int(input())):
#     A,B = map(int,input().split())
#     visited = [0]*10000
#     q = deque([A])
#     visited[A]=1
#     while q:
#         try:
#             v = q.popleft()
#             for oper in funcs:
#                 nv = funcs[oper](v)
#                 if visited[nv]==0:
#                     visited[nv] = (oper,v) #ㅋ 별 쑈를 다했는데 방문체크를 깜빡한거네 ㅋㅋㅋㅋㅋㅋㅋ
#                     q.append(nv)
#                     if nv == B:
#                         raise Exception
#         except:break
#         #여기서 hist를 구하는 연산이 오래걸림
#         #hist 구하는 연산을 따로 백트래킹 방식으로 때어내면 시간 단축 가능
#         #백트래킹도 그냥하는게 아니라 적어도 순번같은건 기억해야함.
#         #아니면 뭘로 왔는지 정도.
#         #신박한 코드를 봤으니 비슷하게 해보자!
#     x = B
#     ans = ''
#     while x!=A:
#         y,x = visited[x]
#         ans = y + ans
#     print(ans)

#이상하게 위처럼 하면 시간이 줄긴하는데 획기적으로 줄지가 않는다 왜일까??
#함수 호출에서 시간을 잡아먹나 ????
#호출하지말고 바로계산때려보자
#연산은 함수로 저장하는게 더 빠르고, try:exept가 더 빠르다.ㅠ
#결론은 아무래도 que에 넣을때 저렇게 1개 이상의 원소를 다루면 급격히 느려진다는 것?
from collections import deque
for t in range(int(input())):
    A,B = map(int,input().split())
    visited = [0]*10000
    q = deque([A])
    visited[A]=1
    while q:
        v = q.popleft()
        d = (v*2)%10000
        if visited[d]==0:
            visited[d] = ('D',v)
            if d==B:break
            q.append(d)

        s = (v - 1) % 10000
        if visited[s]==0:
            visited[s] = ('S',v)
            if s==B:break
            q.append(s)

        l = sum(divmod(v * 10, 10000))
        if visited[l]==0:
            visited[l] = ('L',v)
            if l==B:break
            q.append(l)

        t1, t2 = divmod(v, 10)
        r = t2 * 1000 + t1
        if visited[r]==0:
            visited[r] = ('R',v)
            if r==B:break
            q.append(r)
    x = B
    ans = ''
    while x!=A:
        y,x = visited[x]
        ans = y + ans
    print(ans)