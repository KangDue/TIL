import sys
sys.stdin = open('input.txt')
"""
NxN 행렬의 B제곱 결과
80%에서 틀려버림.. 실화 ??
삘이 b==1 일때 바로 return A를 때려버려서 그런거 같다. %1000안해줘서
받아올때 1000나머지로 받아오게 수정 -> PASS
"""
#행렬을 곱해 봅시다~
def mul(A,B):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += (A[i][k]%1000)*(B[k][j]%1000)
            result[i][j] %= 1000
    return result

def square(A,b):
    if b==1:
        return A
    if b%2:#홀수승
        return mul(square(mul(A,A),b//2),A)
    else:
        return square(mul(A,A),b//2)


n,b = map(int,input().split())
A = [[*map(lambda x:int(x)%1000,input().split())] for _ in range(n)]
for i in square(A,b):
    print(*i)
