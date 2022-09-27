import sys
sys.stdin = open('input.txt')
"""
N과 M
중복허용,
비내림차순 = 수열 하나가 정렬된 형태.(오름차순)
"""
def gen(arr,m):
    for i in range(len(arr)):
        if m == 1:
            yield [arr[i]]
        else:
            for e in gen(arr[i:],m-1):
                yield [arr[i]] + e
n,m = map(int,input().split())
for i in gen(range(1,n+1),m):
    print(*i)
