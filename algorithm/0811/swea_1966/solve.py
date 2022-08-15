import sys
sys.stdin = open('input.txt')
def qs(x):
    if len(x) <= 1:
        return x
    else:
        pivot = x.pop(len(x)//2)
        less = [i for i in x if i<pivot]
        great = [i for i in x if i>= pivot]
        return qs(less) + [pivot] + qs(great)
T = int(input())
for t in range(1,T+1):
    n = int(input())
    nums = list(map(int,input().split()))
    ans = qs(nums)
    ans = str(ans)[1:-1].replace(",","")
    print(f'#{t} {ans}')