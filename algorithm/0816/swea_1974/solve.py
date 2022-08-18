import sys
sys.stdin = open('input.txt',encoding='utf-8')

#9 팩토리얼 362880
from functools import reduce
for t in range(1,int(input())+1):
    sudoku = []
    for i in range(9):
        sudoku.append(list(map(int,input().split())))
    error = False
    for i in range(9): # 행 확인
        if reduce(lambda x,y:x*y,sudoku[i]) != 3.6288e+5: error = True; break
        temp = []
        for j in range(9): # 열 확인
            temp.append(sudoku[j][i])
        if reduce(lambda x,y:x*y,temp) != 3.6288e+5: error = True; break
        if i%3 == 0: # 작은 사각형 확인
            for j in range(0,9,3): #각 square 시작 점 ( 3x3 )
                temp = []
                for k in range(3):
                    for z in range(3):
                        temp.append(sudoku[i+k][j+z])
                if reduce(lambda x,y:x*y,temp) != 3.6288e+5: error = True; break
            if error:
                break
    if error: print(f'#{t} 0')
    else: print(f'#{t} 1')#이상 없으면




