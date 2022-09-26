print("제네레이터")
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
print("bit 부분집합")
arr = [1,2,3,4,5]
#binary를 이용한 부분집합 만들기
for i in range(1<<len(arr)):
    temp = []
    for j in range(len(arr)):
        if i & (1<<j):
            temp.append(arr[j])
    print(temp)
print("------------")
print("my origin 부분집합")
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
print("comb와 섞은 부분집합")
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
print("백트래킹 부분집합.")
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
print("백트래킹 순열")
temp = []
arr =[1,2,3]
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
                temp.pop()
                visited[i] = 0

permu()
print("-----------")
print("그리디 베이비 진")
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
print("병합정렬")
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
print("퀵정렬")
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
print("이진탐색")
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
print("-----------")
print("전위순회")
v=13
ip = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
tree = [[0,0] for _ in range(v+1)]
ip = [*map(int,ip.split())]
for i in range(0,v-1,2):
    if tree[ip[i]][0]:
        tree[ip[i]][1] = ip[i+1]
    else:
        tree[ip[i]][0] = ip[i+1]
def preorder(x):
    print(x,end=' ')
    if tree[x][0]:
        preorder(tree[x][0])
    if tree[x][1]:
        preorder(tree[x][1])
preorder(1)
    
print("\n-----------")
print("재귀 선택정렬")
arr = [3,5,1,2,4]
def selection_sort(n,idx=0):
    global arr
    if idx == n:
        return 0
    mindex = idx
    for i in range(idx,len(arr)):
        if arr[mindex] > arr[i]:
            mindex = i
    if idx != mindex:
        arr[idx], arr[mindex] = arr[mindex] , arr[idx]
    selection_sort(n,idx+1)
selection_sort(5)
print(arr)
print("-----------")
def permu2(n,k):
    if n == k:
        print(arr)
    else:
        for i in range(n,k):
            arr[n],arr[i] = arr[i],arr[n]
            permu2(n+1,k)
            arr[n], arr[i] = arr[i], arr[n]
permu2(0,5)



