import sys
sys.stdin = open('input.txt')
T = int(input())
for t in range(1,T+1):
    n,q= map(int,input().split())
    task = [list(map(int,input().split())) for i in range(q)]
    cards = [0 for i in range(n+1)]
    for i in range(q):
        a, b = task[i][0],task[i][1]
        cards[a:b+1] = [i+1]*(b-a+1)
    cards = cards[1:]
    cards = str(cards)[1:-1].replace(",","")
    print(f'#{t} {cards}')
