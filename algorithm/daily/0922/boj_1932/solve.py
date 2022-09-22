import sys
sys.stdin = open('input.txt')
"""
정수 삼각형
맨 위 층에서 맨 아래층으로 내려올때
대각선 아래 숫자만 고를수 있다칠때
최대값을 구하시오
"""
n = int(input())
pym = [[0]]+[[0]+[*map(int,input().split())] for _ in range(n)]
#잘 생각해보니 딱 dp 각이라 해봄.
for i in range(1,n+1):
    for j in range(1,i+1):
        temp = []
        if j==i:
            pym[i][j] += pym[i-1][j-1]
        else:
            pym[i][j] += max(pym[i-1][j],pym[i-1][j-1])
print(max(pym[n]))
