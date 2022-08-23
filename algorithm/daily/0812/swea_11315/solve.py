import sys

sys.stdin = open('input.txt', encoding='utf-8')

def noc(line):
    count =0
    for i in line: #한줄에서
        if i=="o":
            count += 1 #연속인 갯수 카운트
        else:
            if count > 4: # 97개 달성... 3개 어디갔냐
                return True
            count = 0 #초기화
    if count > 4: # 연속 5개부터는 True 반환
        return True

def check(x):
    for i in x:
        for k in i:#count를 쳐 넣어버리면 숫자만 세버림... (연속인것! 이 중요.)
            if noc(k): #5개만 찾다가 5개 이상도 했는데...
                return 1 # 50몇개 정답에서 81개로 늘었다.

T = int(input())
for t in range(1,T+1):# 완성된 오목이 있는지 판별
    n = int(input()) # nxn 크기 오목판 돌='o'(소문자 오)
    grid = [list(input()) for i in range(n)] # 빈 곳은 '.' (마침표)
    #가능한 case 행,열, 대각선1,2
    grid1 = [[0]*(n-i)+grid[i]+[0]*i for i in range(n)]
    grid2 = [[0]*i+grid[i]+[0]*(n-i) for i in range(n)]
    checklist=[grid,zip(*grid), zip(*grid1), zip(*grid2)]
    for i in grid1:
        print(i)
    if check(checklist):
        print(f'#{t} YES')
    else:
        print(f'#{t} NO')

# T = int(input())
# for t in range(1,T+1):# 완성된 오목이 있는지 판별
#     n = int(input()) # nxn 크기 오목판 돌='o'(소문자 오)
#     grid = [input() for i in range(n)] # 빈 곳은 '.' (마침표)
#     dae1 = ""
#     dae2 = ""
#     for i in range(n):
#         if grid[i].find("ooooo") > -1 :
#             print(f'#{t} YES')
#         col=""
#         dae1 += " " + grid[i][i]
#         dae2 +=
#         for k in range(n):
#             col += " "+grid[k][i]+" "
#             dae1 += grid[i][i]