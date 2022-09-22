import sys
sys.stdin = open('input.txt')
"""
퀵 정렬
퀵 정렬을 구현해 N개의 정수를 정렬하고 = A list
A[N//p2]에 저장된 값을 출력하자
qs 는 작성이 간편함 하지만, 메모리 and 속도 issue
qs2는 작성이 어렵지만 정석적인 qs(빠름, 메모리 절약)
"""

def qs(arr):
    if len(arr)<=1:
        return arr
    pivot = arr.pop()
    lower,upper = [],[]
    for i in arr:
        if i <= pivot : lower.append(i)
        else: upper.append(i)
    return qs(lower)+[pivot]+qs(upper)

def qs2(x,s,e): # 배열, 시작점, 끝점
    if s >= e: # 원소가 1개일 때
        return
    pivot = s #Hoare (호어) 분할
    left = pivot + 1
    right = e
    while left <= right: # 서로 교차하기 전 까지
        #인덱스를 초과하지 않고 피벗보다 큰값을 찾을 때 까지
        while left <= right and x[left] <= x[pivot]:
            left += 1
        #left와 반대
        while left <= right and x[right] >= x[pivot]:#피벗은 포함하지 않음
            right -= 1
        if left > right: #교차 했다면 피벗을 작은 값과 교체한다. 이러면 while도 끝남. = 각 파티션 정렬 끝
            #작은값(right)가 왼쪽으로 가바렸으니
            x[pivot], x[right] = x[right], x[pivot]
        else: #교차 안한 정상 상태면
            x[left], x[right] = x[right], x[left]
        #이후 partition된 왼쪽과 오른쪽 부분 각각에 대해서 정렬 수행
    qs2(x, s, right - 1)
    qs2(x, right + 1, e)

for t in range(int(input())):
    n = int(input())
    A = [*map(int,input().split())]
    qs2(A,0,n-1)
    print(f'#{t+1} {A[n//2]}')