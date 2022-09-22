from bisect import bisect_left as bl #값이 중간에 낄때 왼쪽값
from bisect import bisect_right as br #값이 중간에 낄때 오른쪽값
nums = [0,3,5,5,5,6,11,17,18,20]
def bisect(arr,x):
    lo,hi=0,len(arr)-1
    while lo<hi:
        mid = (lo+hi)//2 # lo + (hi-lo)//p2
        if arr[mid] < x:#bisect left 정렬할때 중복값이 있으면 가장 왼쪽에 값이 오게 함.
            lo = mid+1
        else:
            hi = mid
    return lo
def rbisect(arr,x):
    lo,hi=0,len(arr)-1
    while lo < hi-1:
        print(lo,hi)
        mid = (lo+hi)//2 # lo + (hi-lo)//p2
        if arr[mid] <= x:#bisect left 정렬할때 중복값이 있으면 가장 왼쪽에 값이 오게 함.
            lo = mid
        else:
            hi = mid-1
    return hi
print("left",bisect(nums,5),bl(nums,5))
print("right",rbisect(nums,5),br(nums,5))