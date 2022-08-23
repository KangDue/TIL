import sys
sys.stdin = open('input.txt')

def filt(i,k,step):
    global grid
    if grid[i][k] != "#":
        return False
    else:
        try:
            if grid[i][k+2*step] == "#" and grid[i+step][k+step] == "#":
                return True
            else:
                return False
        except:
            return False

def evenfilt(i,k,step):
    global grid
    if grid[i][k] != "#":
        return False
    else:
        try:
            if step == 1 or k - step +1 < 0:
                return False
            elif grid[i+step][k+step] == "#" and grid[i+step+1][k-step+1] == "#":
                return True
            else:
                return False
        except:
            return False

for t in range(1,int(input())+1):
    h,w = map(int,input().split())
    grid = [input() for i in range(h)]
    tgrid = list(zip(*grid))
    tgrid = [''.join(i) for i in tgrid]
    c = 0
    for i in range(h):#정
        for step in range(1,w//2+1):
            for k in range(w-2*(step-1)):
                if filt(i,k,step):
                    c += 1
                if evenfilt(i,k,step):
                    c += 1

    grid.reverse()
    for i in range(h):#정
        for step in range(1,w//2+1):
            for k in range(w-2*(step-1)):
                if filt(i,k,step):
                    c += 1
                if evenfilt(i,k,step):
                    c += 1
    grid = tgrid
    for i in range(w):#Transpose
        for step in range(1,h//2+1):
            for k in range(h-2*(step-1)):
                if filt(i,k,step):
                    c += 1
                if evenfilt(i,k,step):
                    c += 1
    grid.reverse()
    for i in range(w):#Transpose
        for step in range(1,h//2+1):
            for k in range(h-2*(step-1)):
                if filt(i,k,step):
                    c += 1
                if evenfilt(i,k,step):
                    c += 1
    print(f'#{t} {c}')