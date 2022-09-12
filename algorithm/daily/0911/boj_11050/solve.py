import sys
sys.stdin = open('input.txt')
import math
print(math.comb(*map(int,input().split())))