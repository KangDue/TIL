import sys
sys.stdin = open('input.txt')
read = sys.stdin.readline
n,x=map(int,read().split())
nums=map(int,read().split())
print(*filter(lambda y:y<x,nums))