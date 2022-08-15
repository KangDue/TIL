import sys
sys.stdin = open('input.txt')
T = int(input())
for t in range(1,T+1):
    day = input()
    #월~일
    days = dict(MON=6,TUE=5,WED=4,THU=3,FRI=2,SAT=1,SUN=7)
    print(f"#{t} {days[day]}")