import sys
sys.stdin = open('input.txt')
T = int(input())
for t in range(1,T+1):
    ball = input()

    base = 0
    while ball.find("(") > -1:
        idx = ball.find("(")
        ball = ball[:idx]+ball[idx+2:]
        base += 1

    while ball.find(")") > -1:
        idx = ball.find(")")
        ball = ball[:idx] + ball[idx + 2:]
        base += 1

    print(f'#{t} {base}')