import sys
sys.stdin = open('input.txt')
"""
피보나치수 6
행렬, 분할정복
동섭이의 선형대수학 강의, 점화식을 행렬의 곱으로 나타내기
"""
n = int(input())
A = [[1,1],[1,0]]
x = [1,0]
def matmul(a,b):
    grid = [
            [(a[0][0]*b[0][0] + a[0][1]*b[1][0])%1000000007,(a[0][0]*b[0][1] + a[0][1]*b[1][1])%1000000007],
            [(a[1][0]*b[0][0] + a[1][1]*b[1][0])%1000000007,(a[1][0]*b[0][1] + a[1][1]*b[1][1])%1000000007]
            ]
    return grid
def square(arr,n):
    if n <= 0:
        return 1
    if n == 1:
        return arr
    if n%2: #홀수면
        return matmul(square(matmul(arr,arr),n//2),arr)
    else:
        return square(matmul(arr,arr),n//2)
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    print(square(A,n-1)[0][0])
