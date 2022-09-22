import sys
sys.stdin = open('input.txt')

T =int(input())
for t in range(1,T+1):
    #10개의 정수를 줌
    nums = tuple(map(int,input().split()))
    for i in range(1,1<<10): #1~ p2**10 -1 까지
        comb = f'{i:010b}' #이진수 형태 생성
        hap = 0
        for k in range(10): # 계산
            if comb[k] == "1":
                hap += nums[k]
        if hap == 0:
            print(f'#{t} 1')
            break
    else:
        print(f'#{t} 0')
