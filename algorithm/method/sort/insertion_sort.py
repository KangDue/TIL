def insertion_sort(x,n):
    for i in range(1,n): #첫 원소는 정렬 상태라 가정한다. ( n=1이면 원상태 그대로)
        for k in range(i-1,-1,-1): # i-1 부터 0까지 역순
            if x[i] < x[k]: # 자기보다 큰놈 나올때까지 계속 바꿔가며 전진
                x[i], x[k] = x[k], x[i] # 자기가 가장 작으면 가장 앞에 삽입된 형태가 됨
            else:
                break
    return x
x = list(range(10,0,-1))
print(insertion_sort(x,3))# n = n개 요소까지 정렬된 상태.
#selection sort처럼 몇개씩 정렬할지 고를 수 있다.
#시간 복잡도는 O(n^2)지만 거의 다 정렬된 상태면 아주 빠름.
