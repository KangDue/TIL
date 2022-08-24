import sys
sys.stdin = open('input.txt')

for t in range(int(input())):
    n,m = map(int,input().split())
    nums = input().split()
    print(f'#{t+1}',nums[m%n])