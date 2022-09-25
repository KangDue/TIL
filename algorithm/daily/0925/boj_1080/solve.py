import sys
sys.stdin = open('input.txt')
"""
행렬 A를 B로 바꾸는데 필요한 최소 연산횠수
연산은 3x3 서브 행렬 전체 뒤집기만 가능
복잡하게 생각할거없이 순서대로 같으면 놔두고 다르면 뒤집어야한다.
"""
def op(r,c):
    global A
    for i in range(r,r+3):
        for j in range(c,c+3):
            A[i][j] ^= 1

n,m=map(int,input().split())
A = [[*map(int,input())] for _ in range(n)]
B = [[*map(int,input())] for _ in range(n)]
if n < 3 or m < 3:
    if A==B:
        print(0)
    else:
        print(-1)
else:
    c = 0
    try:
        for i in range(n):
            for j in range(m):
                if A[i][j] != B[i][j]:
                    if i+3 > n or j+3 > m:
                        print(-1)
                        raise Exception
                    else:
                        op(i,j)
                        c+=1
        else:
            print(c)
    except:
        pass
