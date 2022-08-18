import sys
sys.stdin = open('input.txt',encoding='utf-8')

for t in range(1, int(input())+1):
    n = int(input())
    prices = list(map(int,input().split()))
    sur = 0
    while prices: #최고가 인날 찾아서 그 앞은 다팔기 반복:
        mp = max(prices)
        mp_index = prices.index(mp)
        sur += mp*mp_index - sum(prices[:mp_index])
        prices = prices[mp_index+1::]
    print(f'#{t} {sur}')