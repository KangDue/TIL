import sys
sys.stdin = open('input.txt')
def steps(i):
    global snail, a, b
    if mode == 1:
        snail[a][b] = i
        b += 1
    elif mode == 2:
        snail[a][b] = i
        a += 1
    elif mode == 3:
        snail[a][b] = i
        b -= 1
    elif mode == 4:
        snail[a][b] = i
        a -= 1
        if snail[a][b]:
            a += 1
            b += 1
T =int(input())
for t in range(1,T+1):
    n = int(input())
    snail = [[0 for i in range(n+1)] for k in range(n+1)]
    direction = {1:2, 2:3, 3:4, 4:1} # 방향 전환
    mode = 1 #방향 모드
    c = 0 #모든 방향 순환 횟수
    a,b = 1,1 # 좌표
    step = n - 1 #방향별 가는 스텝수
    x = 0 #넣을 값
    while 1:
        if x == n**2: # 값 다차면 종료
            break
        for k in range(step): # 방향별 step씩 반복
            x += 1
            steps(x)
            if x == n**2: # 값 다차면 종료
                break
        else: # 방향별로 다 돌면
            c += 1 # 순환 획수
            mode = direction[mode] # 방향 변경
        if c == 4: # 4방향 다돌면
            step = step - 2 if step > 2 else 1
            c = 0 # 순환 횟수 초기화
    snail = [snail[i][1:] for i in range(1,n+1)] #0빼고 추출
    print(f'#{t}')
    for i in snail:
        print(str(i)[1:-1].replace(",",""))