import sys
sys.stdin = open('input.txt')
def infind(x):
    if x > n: return 0
    infind(2 * x)
    if not arr[x]:
        arr[x] = nums.pop()
    infind(2 * x + 1)
for t in range(int(input())):
    n = int(input())
    nums = list(range(n,0,-1))
    arr = [0]*(n+1)
    infind(1)
    print(f'#{t+1}',arr[1],arr[n//2])