import sys
sys.stdin = open('input.txt')

#수의 범위가 절대값이다...
#카운팅 소트
n = int(input())
nums = [0]*2000001
for i in range(n):
    nums[int(input())] += 1

arr = list(filter(lambda x:nums[x],range(-1000000,1000001)))
print(*arr,sep='\n')

#