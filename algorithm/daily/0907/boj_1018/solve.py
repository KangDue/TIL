import sys
sys.stdin = open('input.txt')
R, C = map(int,input().split())
grid = [input() for _ in range(R)]
#grid에서 8x8로 아무데부터 잘라서 최소로 색칠해 체스판 완성할때
#다시 칠해야하는 칸의 최소 개수
#체스판 시작 색을 잘라온 것에서 고정하면 안되고, W,B중 최소값을 골라야함.

def line_check(arr,start,row):
    pattern = 'WB' if start =='W' else 'BW'
    pattern = pattern[::-1] if row%2 else pattern #홀수행이면 반대
    count = 0
    for k in range(0,8,2):
        if arr[k] != pattern[0]:
            count += 1
        if arr[k+1] != pattern[1]:
            count += 1
    return count

def check(i,j):
    temp = [grid[ii][j:j+8] for ii in range(i,i+8)]
    fc1,fc2 = 0,0
    for row in range(8):
        fc1 += line_check(temp[row],'B',row)
        fc2 += line_check(temp[row],'W',row)
    return min(fc1,fc2)
minv = 64
for i in range(R-8+1):
    for j in range(C-8+1):
        minv = min(minv, check(i,j))
print(minv)