import sys
sys.stdin = open('input.txt')
n=int(input())
nums=[*map(int,input())]
print(sum(nums))