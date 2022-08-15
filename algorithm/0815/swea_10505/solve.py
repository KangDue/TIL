import sys
sys.stdin = open('input.txt',encoding='utf-8')

a = []
for t in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int,input().split()))
    nums = [i for i in nums if i <= sum(nums)/n]
    a.append(f'#{t} {len(nums)}')
print(*a, sep="\n")