import sys
sys.stdin = open('input.txt')
"""
LCS 최장 공통 부분 수열
그냥 공통원소의 개수가 아님! 바로틀렸다 ㅋㅋ
순서가 있는 부분수열 ex) abcdef 의 부분수열 중 하나 acf
"""
from itertools import combinations as cb
a = input()
b = input()
A