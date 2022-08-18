def quick_sort_1(x,s,e): # 배열, 시작점, 끝점
    if s >= e: # 원소가 1개일 때
        return
    pivot = s #Hoare (호어) 분할
    left = pivot + 1
    right = e
    while left <= right: # 서로 교차하기 전 까지
        #인덱스를 초과하지 않고 피벗보다 큰값을 찾을 때 까지
        while left <= e and x[left] <= x[pivot]:
            left += 1
        #left와 반대
        while right > s and x[right] >= x[pivot]:#피벗은 포함하지 않음
            right -= 1
        if left > right: #교차 했다면 피벗을 작은 값과 교체한다. 이러면 while도 끝남. = 각 파티션 정렬 끝
            #작은값(right)가 왼쪽으로 가바렸으니
            x[pivot], x[right] = x[right], x[pivot]
        else: #교차 안한 정상 상태면
            x[left], x[right] = x[right], x[left]
        #이후 partition된 왼쪽과 오른쪽 부분 각각에 대해서 정렬 수행
    quick_sort_1(x, s, right - 1)
    quick_sort_1(x, right + 1, e)

a = [5,1,25,6542,34,2,5]
quick_sort_1(a,0,len(a)-1)
print(a)


# 1번 sort는 너무~ 길고 pythonic 하지 않음...
# pythonic 하게 해보자!
def quick_sort_2(x):
    if len(x) <= 1: #빈 리스트일 수도 있음
        return x
    else:
        pivot = x.pop()#호어법은 아니고 편하게 마지막 값 쓰기
        left = [i for i in x if i <= pivot]
        right = [i for i in x if i > pivot]
        return quick_sort_2(left) + [pivot] + quick_sort_2(right)
print(quick_sort_2(a))

# 평균적인 시간복잡도는 nlogn 이지만 최악은 n^2
# 이미 정렬된 녀석의 맨앞 값을 pivot으로 삼으면 최악이 되기도함.
# 그래서 평균적인 시간을 보장해 주기위해 라이브러리는 pivot 값 선정 알고리즘이 따로 있음
# 추가로 여러 정렬을 섞어 쓰기도 함.