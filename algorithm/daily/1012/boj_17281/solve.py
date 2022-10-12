"""
야구~
N이닝 진행되며,
이닝당 공수가 교대된다.
9번타자까지 공을 치며 3아웃 안되면 1번타자가 다시 타석에 선다.
타순은 이닝이 변경되어도 순서가 유지된다.
안타 = 한루씩 = 1
2루타 = 2루씩 = 2
3루타 = 3루씩 = 3
홈런 = 전부 홈으로 = 4
아웃 = 아웃 = 0
9명까지 1~N번 선수가 있고 이 선수들의 타순을 부여하자.
각 선수가 각 이닝에서 어떤 결과를 얻은지는 미리 알고 있다.
가장 많은 득점을 하는 타순을 구하자.
딱- 봐도 백트래킹
시간 초과가 뜨는데 이건 순열 생성할 때 같은 것들도 교환 하면서 시간을 낭비해서 그럼.
어떻게 이걸 해결할까?
그게 아니라 점수 매기는 방식이 문제인걸까??
#아웃 선수들은 최대한 뒤에 있어야함.... 는 이닝마다 점수가 달라서 힘들고
시간 줄인다고 줄였는데 50퍼에서 초과

#값을 무조건 저장해서 쓰는거보다 간단한 + 연산 같은 결과는 그자리마다 하는게 나을수도...
범위 연산자는 논리연산자보다 많이 느림.
시간을 극한으로 줄이려면 배열 계산도 최대한 줄이고 변수로 대체 가능하다면
대체하고, 조건도 많이 나오는것 고려 순서를 잘 정해야한다.
"""
import sys,time
# sys.stdin = open('input.txt')

a = time.time()

from itertools import permutations as pm
o = open('input.txt')
n = int(next(o))
res = list(map(lambda x:[*map(int,x.split())],o))
maxv = 0
def get_score(start,order,res):
    home=0
    for ini in res:
        out = 3
        one=two=thr=0
        for idx in range(start,50):
            if not out:
                start = idx%9
                break
            temp = ini[order[idx%9]]
            if not temp:#유효타
                out -= 1
            elif temp==1:
                home += thr
                thr,two = two,one
                one=1
            elif temp==2:
                home += thr+two
                thr=one
                two=1
                one=0
            elif temp==3:
                home += one+two+thr
                thr = 1
                one=two=0
            elif temp==4:
                home += one+two+thr+1
                one=two=thr=0
    return home
for permu in pm(range(1,9),8):
    order = [*permu[:3],0,*permu[3:]]
    maxv = max(maxv,get_score(0,order,res))
print(maxv)
b = time.time()
print(b-a,"sec")

"""
기존보다 2배는 빠른데 ,서버에서는 1퍼 시간초과뜸 ;; 뭐지
from sys import stdin
from itertools import permutations as pm
o = open('input.txt')
n = int(next(o))
# res = [[*map(int,next(stdin).split())] for _ in range(n)] #각 이닝별 결과
res = list(map(lambda x:[*map(int,x.split())],o))
#각 이닝에는 적어도 한명이 아웃을 한다.
maxv = 0
def get_score(start,order,res):
    cnt = 0
    for ini in res:
        out = 3
        base = 0
        for idx in range(start,50):
            if not out:
                start = idx%9
                break
            temp = ini[order[idx%9]]
            if temp:#유효타
                base <<= temp
                base += 1<<(temp-1)
            else: #아웃
                out -= 1
        cnt += bin(base)[:-3].count('1')
    return cnt
for permu in pm(range(1,9),8):
    order = [*permu[:3],0,*permu[3:]]
    cnt = get_score(0,order,res)
    maxv = max(maxv,cnt)
print(maxv)

"""

    # 해당 이닝 점수와, 다음 이닝 시작 타자

# temp = []
# arr =range(1,9)
# ran = range(8)
# visited = [0]*len(arr)
# def permu(r=0):
#     global maxv,res,temp
#     if r == 8:
#         base = [0]*4
#         start = 0
#         for ini in res: # 한 순열에서, n 이닝게임 실시
#             start = get_score(start,ini,temp,base)
#         maxv = max(maxv,base[0])
#         return 0
#     else:
#         for i in ran:
#             if not visited[i]:
#                 visited[i] = 1
#                 temp.append(arr[i])
#                 if len(temp) == 3:
#                     temp.append(0)
#                 permu(r+1)
#                 if temp[-1] == 0:
#                     temp.pop()
#                 temp.pop()
#                 visited[i] = 0
# permu()
# print(maxv)

# 1번 선수는 4번타자로 fix.... 깜빡하지 말자
# for permu in pm(range(1,9),8):
#     order = [*permu]
#     order.insert(3,0)
#     base = [0]*4
#     start = 0
#     for ini in res: # 한 순열에서, n 이닝게임 실시
#         start = get_score(start,ini,order)
#     maxv = max(maxv,base[0])
# print(maxv)


# arr = [1,2,3,0,4,5,6,7,8]
# def permu2(m,k):
#     global maxv,arr
#     if m == k:
#         start = 0
#         ans = 0
#         for i in range(n): # 한 순열에서, n 이닝게임 실시
#             score, start = get_score(start,i,arr)
#             ans += score
#         maxv = max(maxv,ans)
#     else:
#         for i in range(m,k):
#             if m == 3:
#                 permu2(m+1,k)
#                 break
#             elif i==3:
#                 continue
#             else:
#                 if arr[m] == arr[i]:
#                     arr[m],arr[i] = arr[i],arr[m]
#                     permu2(m+1,k)
#                     arr[m], arr[i] = arr[i], arr[m]
#                 else:
#                     permu2(m + 1, k)
# permu2(0,9)
# print(maxv)

#
# def get_score(start, ini, order):#해당 이닝에서 얻을 수 있는 점수
#     #res[ini] # 해당 이닝 state
#     out = 3
#     base = [0]*4
#     while out:
#         temp = res[ini][order[start]]
#         if temp:#유효타
#             if temp == 4: #홈런
#                 for i in range(1,4):
#                     if base[i]:
#                         base[0]+= 1
#                 base[1:] = [0,0,0]
#                 base[0] += 1
#             else:
#                 for i in range(3,0,-1): # 나머지인데 오름차순하면 중복해서 증가시켜버림
#                     if base[i]:
#                         nb = i+temp
#                         if nb > 3:
#                             base[0] += 1
#                             base[i] -= 1
#                         else:
#                             base[nb] += 1
#                             base[i] -= 1
#                 base[temp] += 1
#         else: #아웃
#             out -= 1
#         start = (start + 1)%9 # 다음 타자.
#     return base[0],start # 해당 이닝 점수와, 다음 이닝 시작 타자