import sys
sys.stdin = open('input.txt',encoding='utf-8')

T = int(input())

for t in range(1,T+1):
    temp = list(set(input()))
    if len(temp) == 2:
        print(f'#{t} Yes')
    else:
        print(f'#{t} No')
#이게 왜 d3??? (python용은 아닌듯, 탐색 알고리즘 연습용)
#set 안써도 충분히 구현가능



