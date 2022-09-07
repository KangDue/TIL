import sys
sys.stdin = open('input.txt')
print(max(map(lambda x:int(x[::-1]),input().split())))