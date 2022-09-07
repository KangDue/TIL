import sys
sys.stdin = open('input.txt')
n = int(input())
nums = [*map(int,input().split())]
maxv = max(nums)
avg = sum(map(lambda x: x/maxv*100, nums))/n
print(avg)
