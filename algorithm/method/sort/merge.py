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