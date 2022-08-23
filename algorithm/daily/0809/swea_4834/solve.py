import sys
sys.stdin = open('input.txt')

#가장 많이 적힌 수와 그 장수
T = int(input())
for t in range(1,T+1):
    n = int(input()) #카드 장수
    cards = list(map(int,input()))
    count = [0 for i in range(10)]
    for i in cards:
        count[i] += 1
    ans = [(count[i],i) for i in cards]
    a = (0,0)
    for i in ans:
        if a[0] < i[0]:
            a = i
        elif a[0] == i[0]:
            if a[1] < i[1]:
                a = i
    print(f'#{t} {a[1]} {a[0]}' )