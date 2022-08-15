import sys
sys.stdin = open('input.txt')

for t in range(1,10+1):
    T = int(input())
    grid = [list(map(int,input().split())) for k in range(100)]
    dae_1 = sum([grid[i][i] for i in range(100)])
    dae_2 = sum([grid[i-1][-i] for i in range(1,101)])
    row = [sum(i) for i in list(zip(*grid))]
    grid =  [ sum(i) for i in grid] + row + [dae_1] + [dae_2]

    ans = 0
    for i in grid:
        if ans < i:
            ans = i
    print(f'#{T} {ans}')

