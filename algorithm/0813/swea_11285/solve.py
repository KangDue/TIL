import sys
sys.stdin = open('input.txt',encoding='utf-8')

from math import ceil,sqrt
answers = []
for t in range(1, int(input())+1):
    ans = 0
    for i in range( int(input()) ):
        x,y = map(int,input().split())
        r = ceil(sqrt(x*x + y*y)/20) if (x,y) != (0,0) else 1 #연산을 통한 abs(x)+abs(y) == 0 보다 그대로 비교하는게 빠르다.
        # ans += 11-r if r<= 11 else 0 #이렇게 무언가를 걍 더해주는 if 문 +연산 둘다 하는것 보단
        if r < 12:#이 방법이 시간을 더 아낀다.
            ans += 11-r
    answers.append(f'#{t} {ans}')
print(*answers,sep="\n")

#
# import math
#
# answers = []
# for tc in range(1, int(input()) + 1):
#     n = int(input())
#     answer = 0
#     for _ in range(n):
#         x, y = map(int, input().split())
#         r = math.ceil(math.sqrt(x * x + y * y) / 20)
#         if r <= 0:
#             answer += 10
#         elif r <= 11:
#             answer += 11 - r
#     answers.append(f'#{tc} {answer}')
#
# for answer in answers:
#     print(answer)
#