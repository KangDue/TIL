import sys
sys.stdin = open('input.txt')
n = int(input())
nums = [*map(int,input().split())]
print(min(nums),max(nums))