import sys
sys.stdin = open('input.txt')
x = int(input())
if x%4==0 and x%100: print(1)
elif x%400==0: print(1)
else:print(0)