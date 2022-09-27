import sys
sys.stdin = open('input.txt')
"""
N과 M
비내림차순 = 수열 하나가 정렬된 형태.(오름차순)
N개의 숫자가 주어짐.
중복 없이 수열 출력
수열은 사전순(수열 자체는 순열)
"""
def gen(arr,m):
    for i in range(len(arr)):
        if m == 1:
            yield (arr[i],)
        else:
            for e in gen(arr[:i]+arr[i+1:],m-1):
                yield (arr[i],) + e
n,m = map(int,input().split())
nums = sorted(map(int,input().split()))
find = dict()
for i in gen(nums,m):
    if not find.get(i):
        print(*i)
        find[i] = 1

## 숏코딩 참고
import sys
input = sys.stdin.readline
print = sys.stdout.write

n,m = map(int,input().split())
arr = input().split()
arr.sort(key=lambda x:int(x))

chk = [False]*n
nums = [0]*m

def DFS(depth=0,n=n,m=m,arr=arr):
    if depth == m:
            print(" ".join(nums)+"\n")
    else:
        before = -1
        for i in range(n):
            if (not chk[i]) & ((i==0) | (before != arr[i])):
                before = arr[i]
                nums[depth]=arr[i]
                chk[i] = True
                DFS(depth+1)
                chk[i]=False

DFS()