import sys
sys.stdin = open('input.txt', encoding='utf-8')

gugu = [ i*j for i in range(1,10) for j in range(1,10)]
def is_gugu(x):
    global gugu
    return x in gugu

T = int(input())

for t in range(1,T+1):
    if is_gugu(int(input())):
        print(f'#{t} Yes')
    else:
        print(f'#{t} No')




