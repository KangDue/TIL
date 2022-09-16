import sys
sys.stdin = open('input.txt')
for t in range(int(input())):
    N = int(input())
    if N == 1:
        ans = 1
    else:
        for i in range(int(N ** (1 / 3)),N):
            if i**3 == N: ans = i; break
            elif i**3 > N: ans = -1;break
    print(f'#{t+1} {ans}')