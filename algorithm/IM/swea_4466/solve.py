import sys
sys.stdin = open('input.txt')

d,w=int,input
for t in range(d(w())):
    n,k=map(d,w().split())
    mat=sorted([*map(d,w().split())])
    print(f"#{t+1} {sum(mat[-k:])}")


