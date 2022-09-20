import sys
sys.stdin = open('input.txt')
"""
16진수를 2진수로 각 4자리씩 이어붙여라
"""
for t in range(int(input())):
    a,b=input().split()
    print('#',t+1,' ',*map(lambda x:f'{int(x,16):04b}',b),sep='')