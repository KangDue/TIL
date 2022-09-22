import sys
sys.stdin = open('input.txt')
"""
병합정렬을 이용한 오름차순 정렬
리스트 분할시 [0:N//p2], [N//p2:N]으로 분할
두 리스트 병합중 왼쪽 마지막과 오른쪽 마지막 보다 큰 경우의수를 출력
정렬이 끝난 리스트에서 L[N//p2]를 출력
"""
def msort(arr):
    global count
    N = len(arr)
    if len(arr)<=1:
        return arr
    left = msort(arr[0:N//2])
    right = msort(arr[N//2:])
    temp = []
    l=r=0
    if left[-1] > right[-1]:
        count += 1
    while l<len(left) and r<len(right):
        if left[l] <= right[r]:
            temp.append(left[l])
            l+=1
        else:
            temp.append(right[r])
            r+=1
    temp += left[l:]+right[r:]
    return temp

for t in range(int(input())):
    count = 0
    n = int(input())
    nums = [*map(int,input().split())]
    nums = msort(nums)
    print(f'#{t+1} {nums[n//2]} {count}')