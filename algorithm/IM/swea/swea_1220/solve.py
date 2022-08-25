import sys
sys.stdin = open('input.txt')

for t in range(10):
    n = int(input())
    nums = [list(map(int,input().split())) for i in range(n)]
    nums = list(zip(*nums)) #편하게 Transpose
    ans = 0
    for line in nums:
        one = False #1을 봤나?
        for k in line: #if를 여러개 놓는거보다 합칠수 있다면 if elif else로 합치는게 좋다.(쓸데없는 조건문 안감)
            if k == 1: #사실 stack 필요 없을지도 ?
                one = True
            elif one and k == 2: #1을 보고 2를 보면
                one = 0 # 0으로 되돌리고
                ans += 1 # 카운트
    print(f'#{t+1} {ans}')
