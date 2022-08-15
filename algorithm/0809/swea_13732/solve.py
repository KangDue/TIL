import sys
sys.stdin = open('input.txt')

def is_continue(x):
    a = x.find("#")
    b = x.rfind("#")
    if x[a:b+1] == "#"*(b-a+1):
        return True,(b-a+1)
    else:
        return False, 0

T = int(input())
for t in range(1,T+1):
    n = int(input())
    grid = [input() for i in range(n)]
    pattern = ""
    end = False
    for i in range(n): # 좌상단 꼭짓점
        for k in range(n):
            temp1, temp2 = is_continue(grid[i])
            if temp1:
                pos = [i,temp2]
                pattern = grid[i]
                end = True
                break
        if end:
            break

    compare = []
    for i in range(pos[0]):
        compare.append("." * n)
    for i in range(pos[1]):
        compare.append(pattern)
    for i in range(n-len(compare)):
        compare.append("." * n)
    if compare == grid:
        print(f'#{t} yes')
    else:
        print(f'#{t} no')

