import sys
sys.stdin = open('input.txt',encoding='utf-8')

def is_pal(x):
    if len(x)<2: return True
    elif x[0] != x[-1]: return False
    else: return is_pal(x[1:-1])
# n x n 글자판에서 길이가 m인 회문 찾기
T = int(input())
for t in range(1,T+1):
    n, m = map(int,input().split()) #길이가 m인 회문 찾기
    mat = [input() for i in range(n)]
    tmat = ["".join(i) for i in zip(*mat)]
    find = False
    for i in range(n):
        for k in range(n-m+1):
            if is_pal(mat[i][k:k+m]):
                print(f'#{t} {mat[i][k:k+m]}')
                find = True; break
            if is_pal(tmat[i][k:k+m]):
                print(f'#{t} {tmat[i][k:k + m]}')
                find = True; break
        if find: break