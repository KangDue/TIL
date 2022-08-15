import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    # n일간 수강하려면 얼마나 지내야하나?
    # 특정요일만 강의(안열리진 않음)
    #b - a +1
    n = int(input())
    opens = input().replace(" ","")
    idx = [i for i in range(7) if opens[i] == "1"]#강의 열리는 날
    per_week = len(idx)# 한주에 들을 수 있는 횟수
    print(idx)
    temp = opens*2
    c = 0
    for i in range(7):
        if c == n%per_week:
            break
        elif temp[i] == "1":
            c += 1
    c = i#나머지 녀석 인덱스
    7*(n//per_week-2) + (7-)