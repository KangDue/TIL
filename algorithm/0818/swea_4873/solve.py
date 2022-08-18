import sys
sys.stdin = open('input.txt',encoding='utf-8')

for t in range(1,int(input())+1):
    a = list(input())
    i = 0
    while i<len(a)-1: #마지막 하나전 인덱스 까지
        if a[i]==a[i+1]: #반복이면
            del a[i]
            del a[i]
            i = 0 #인덱스 초기화
            continue
        else:
            i += 1
    print(f'#{t} {len(a)}')