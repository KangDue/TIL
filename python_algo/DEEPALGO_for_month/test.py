def a(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            # arr[i+1:] 조합
            # arr[i:] 중복조합
            # arr[:i] + arr[i+1:] = 순열
            # arr 중복 순열
            for e in a(arr[i:],r-1):
                yield [arr[i]] + e
for i in a([1,2,3,4],3):
    print(i)
print("------------")
arr = [1,2,3,4,5]
#binary를 이용한 부분집합 만들기
for i in range(1<<len(arr)):
    temp = []
    for j in range(len(arr)):
        if i & (1<<j):
            temp.append(arr[j])
    print(temp)
print("------------")

subset = []
arr = [3,6,7,1,5,4]
remain = True
def subset(box=[],start=0,pivot=0,n=1):
    global arr,remain
    if len(box)==len(arr):
        remain=False
        print(box)
        return 1
    elif pivot == len(arr):#n개씩 뽑는 기준점. 뽑는 개수 +1
        return subset([], 0, 0, n + 1)
    elif len(box) == n:
        print(box)
        return 1
    if remain:
        for i in range(start,len(arr)): #자신 다음번호부터 선택
            subset(box+[arr[i]],i+1,pivot,n) #원소를 추가, 자기자신 제외 나머지 선택,
            if i+1 == len(arr):  # pivot 기준
                if n==1:
                    return subset([], 0, 0, n+1)
                return subset([], pivot+1, pivot + 1, n)
subset()
print("------------")

def comb(r,idx=0,box = []):
    global arr
    if r == 0:
        print(box)
    for i in range(idx,len(arr)):
        comb(r-1,i+1,box+[arr[i]])
def subset2():
    global arr
    for i in range(len(arr)):
        comb(i)
subset2()
print("------------")
temp = []
def subset3(k=0):
    global temp
    if k == len(arr):
        print(temp)
    else:
        temp.append(arr[k])
        subset3(k+1)
        temp.pop()
        subset3(k + 1)
subset3()

print("------------")
temp = []
visited = [0]*len(arr)
def permu(r=0):
    if r == len(arr):
        print(temp)
        return 0
    else:
        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = 1
                temp.append(arr[i])
                permu(r+1)
                visited[i] = 0
                temp.pop()
permu()
print("-----------")
problem = "123111"
count = [0]*10
for i in problem:
    count[ord(i)-48] += 1
i = 0
run=tri=0
while i<10:
    if count[i] == 3:
        count[i] -= 3
        tri += 1
        continue
    if count[i] >= 1 and count[i+1] >= 1 and count[i+2] >= 1:
        count[i] -= 1
        count[i+1] -= 1
        count[i+2] -= 1
        run += 1
        continue
    i += 1
if run+tri == 2:
    print("WIN")
else:
    print("LOSE")
print("-----------")

def msort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    left = msort(arr[:length//2])
    right = msort(arr[length//2:])

    temp = []
    l=r=0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            temp.append(left[l])
            l += 1
        else:
            temp.append(right[r])
            r += 1
    temp += left[l:] + right[r:]
    return temp


print(msort([3,1,6,4,2,7]))

print("-----------")

def qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left,right,same = [],[],[]
    for i in range(len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
        else:
            same.append(arr[i])
    return qsort(left) + same + qsort(right)

print(qsort([3,1,6,4,2,7]))

print("-----------")

def binary_search(arr,low,high,x):
    mid = (low+high)//2
    while low < high:
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr,mid + 1,high,x)
        else:
            return binary_search(arr, low , mid - 1 , x)
    return -1

temp = [1,2,3,6,8,9,11,15,26,30]
print(binary_search(temp,0,len(temp),26))







