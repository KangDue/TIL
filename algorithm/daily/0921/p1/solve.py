import sys
sys.stdin = open('input.txt')
"""
재귀 선택정렬
"""
arr = [1,5,3,7,3,5,10]
def selection(arr,n,idx=0): #정렬할 배열, 정렬할 원소의 수, 정렬을 시작할 시작점
    if idx >= n-1:
        return 1
    else:
        min_idx = idx
        for i in range(idx+1,len(arr)):
            if arr[min_idx] > arr[i]:
                min_idx = i
        arr[min_idx], arr[idx] = arr[idx],arr[min_idx]
        selection(arr,n,idx+1)
selection(arr,7,0)
print(arr)
