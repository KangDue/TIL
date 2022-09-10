import sys
sys.stdin = open('input.txt')
#블랙잭
#카드합 21내에서 최대 크기 만들기
#변형 블랙잭 합 m 맞추기
#n장의 카드중 3장이 M 이하면서 최대한 가까운 3장의 합 출력
from itertools import combinations as cb
n, m = map(int,input().split())
nums = [*map(int,input().split())]
maxv = 0
for i in cb(nums,3):
    temp = sum(i)
    if maxv < temp and temp <= m:
        maxv = temp
print(maxv)
