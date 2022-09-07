import sys
sys.stdin = open('input.txt')
a,b=map(int,input().split())
hour = range(0,24)
minute = range(0,60)
#45분 앞서게 알람설정, 24시간표기 a=시간, b=분
if b-45 < 0: a = hour[a-1]
b = minute[b-45]
print(a,b)