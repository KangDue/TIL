import sys
sys.stdin = open('input.txt', encoding='utf-8')

sp = [1,4,9,121,484]
a = []
for t in range(1, int(input())+1):
    A, B = map(int, input().split())
    temp = [i for i in sp if A <= i <= B]
    a.append(f'#{t} {len(temp)}')
print(*a, sep="\n")