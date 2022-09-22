import sys
sys.stdin = open('input.txt')
"""
부분집합 만들기
"""
arr = [3,6,7,1,5,4]
remain = True
def subset(arr,ss=[],start=0,pivot=0,n=1):
    global remain
    if len(ss)==len(arr):remain=False;print(ss);return 1
    elif pivot == len(arr):#n개씩 뽑는 기준점. 뽑는 개수 +1
        return subset(arr, [], 0, 0, n + 1)
    elif len(ss) == n: print(ss);return 1
    if remain:
        for i in range(start,len(arr)): #자신 다음번호부터 선택
            subset(arr,ss+[arr[i]],i+1,pivot,n) #원소를 추가, 자기자신 제외 나머지 선택,
            if i+1 == len(arr):  # pivot 기준
                if n==1:
                    return subset(arr, [], 0, 0, n+1)
                return subset(arr, [], pivot+1, pivot + 1, n)
subset([1,2,3,4])