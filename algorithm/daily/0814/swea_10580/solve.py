import sys
sys.stdin = open('input.txt', encoding='utf-8')

a = []
for t in range(1, int(input())+1):
    n = int(input())
    lines = [list(map(int,input().split())) for i in range(n)]
    lines.sort(key=lambda x:x[1])
    c = 0
    for i in range(1,n):
        for j in range(i):
            if lines[i][0] < lines[j][0] and lines[j][1] < lines[i][1]:
                c += 1
    a.append(f'#{t} {c}')
print(*a, sep="\n")