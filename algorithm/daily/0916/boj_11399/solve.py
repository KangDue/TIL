import sys
sys.stdin = open('input.txt')
"""
ATM이 1대있고 그앞에 N명이 줄서있다.(1~N번)
i번이 돈뽑는데 걸리는 시간 Pi
각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값 구하기.
얼핏보면 모든 경우의수 같은 느낌이지만(답을 구할수야 있지만 오래걸림)
오름차순 정렬하면 각자 자기가 기다리는시간 최소가됨 = 결국 누적합의 합 최소
"""
from functools import reduce
n = int(input())
temp = [*map(int,input().split())]
print(sum(map(lambda x:reduce(lambda x,y:x+y,sorted(temp)[:x+1],0),range(n))))
#숫자 2개를 활용