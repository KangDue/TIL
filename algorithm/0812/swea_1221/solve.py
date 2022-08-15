import sys
sys.stdin = open('input.txt',encoding='utf-8')


T = int(input())
for t in range(1, T + 1):
    info = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    (tc, n),text = input().split(), input().split()
    print(f'#{t}')
    print(*sorted(text,key=lambda x:info[x]))
