import sys
sys.stdin = open('input.txt')
T = int(input())
#구구단에 포함되면 답, 아니면 -1 (1x1 ~ 9x9)
#이게 d3?
#포인트좀 퍼줘서 공부하는데 쓰라고 주는 느낌이다.
for t in range(1,T+1):
    a, b = map(int,input().split())
    if a>9 or b>9:
        print(f'#{t} -1')
    else:
        print(f'#{t} {a*b}')