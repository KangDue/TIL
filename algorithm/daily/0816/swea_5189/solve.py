import sys
sys.stdin = open('input.txt', encoding='utf-8')

from itertools import permutations as pm
for t in range(1,int(input())+1):
    n = int(input())
    mat = [list(map(int,input().split())) for i in range(n)]

    minv = n*n*100
    for i in pm(range(1,n),n-1):
        ans = mat[0][i[0]]
        for k in range(1,n-1):
            ans += mat[ i[k-1] ][ i[k] ]
        ans += mat[i[k]][0]
        if minv > ans: minv = ans
    print(f'#{t} {minv}')
