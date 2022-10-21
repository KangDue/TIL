import sys
sys.stdin = open('input.txt')

r, sr = range, sys.stdin.readline
from collections import deque,defaultdict
n,k = map(int,sr().split())

if n==k:
    print(1)
else:
    nums = [0]*500001
    visited = dict()
    q = [[n,k,0]]
    time = 0
    while q:
        new = []
        time += 1
        try:
            for x,y,step in q:
                for nx,ny in ((x+1,y+step+1),(x+1,y-step-1),(x-1,y+step+1),(x-1,y-step-1),(x*2,y+step+1),(x*2,y-step-1)):
                    if 0<=nx<=500000 and 0<=ny<=500000 and not visited.get((ny,nx,step+1)):
                        new.append([nx,ny,step+1])
                        visited[(ny,nx,step+1)] = 1
                        visited[(nx,ny,step+1)] = 1
                        print(nx,ny)
                        if nx==ny:
                            print(time)
                            raise Exception
            q=new
        except:
            break
    else:
        print(-1)