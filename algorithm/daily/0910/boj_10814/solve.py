import sys
#sys.stdin = open('input.txt')
a = open('input.txt')
l = [*map(lambda x:x.split(),a)]
n = int(l[0][0])
l = l[1:]
l = [*map(lambda x: [int(x[0]),x[1]],l)]
# # 1. 내장 정렬 버전
# l = [[i]+l[i] for i in range(1,n+1)]
# l.sort(key=lambda x:(int(x[1]),x[0]))
# for i in l:
#     print(*i[1:])


# p2. 병합정렬 버전
# def msort(arr):
#     if len(arr) < p2:
#         return arr
#     mid = len(arr)//p2
#     lower = msort(arr[:mid])
#     upper = msort(arr[mid:])
#
#     merged = []
#     l = u = 0
#     while l < len(lower) and u < len(upper): #병합하기
#         if lower[l][0] <= upper[u][0]:
#             merged.append(lower[l]); l += 1
#         else:
#             merged.append(upper[u]); u += 1
#     merged += lower[l:]+upper[u:] #나머지 합치기
#     return merged
# temp = msort(l)
#병합정렬 할때 앞에꺼를 기준 이하 범위로 하면 stable
#미만으로하면 unstable ! 잘 판단하는게 좋음


# 3. 삽입정렬 버전 = 시간복잡도가 n**2이라 시간초과뜸
# def insertion_sort(x,n):
#     for i in range(1,n): #첫 원소는 정렬 상태라 가정한다. ( n=1이면 원상태 그대로)
#         for k in range(i,0,-1): # i-1 부터 0까지 역순
#             if x[k][0] < x[k-1][0]: # 자기보다 큰놈 나올때까지 계속 바꿔가며 전진
#                 x[k], x[k-1] = x[k-1], x[k] # 자기가 가장 작으면 가장 앞에 삽입된 형태가 됨
#             else:
#                 break
#     return x
# temp = insertion_sort(l,n)
# for i in temp:
#     print(*i)

# 4. 내장 정렬 버전 stable 한가? 실험
# 결론: stable 하다.
l.sort(key=lambda x:x[0])
for i in l:
    print(*i)