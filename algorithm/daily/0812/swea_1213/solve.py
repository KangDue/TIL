import sys
sys.stdin = open('input.txt', encoding='utf-8')
"""
프리셀 게임 언제나 win/lose 뿐
tot = G, today = D 판 했음. Pg %, Pd %
아무것도 모르는데 아는건 오늘 적어도 N판 했다. (D를 정확히 모름)
이게 말이되면 possible, 안되면 broken
"""
for t in range(1,11):
    T = int(input())
    pattern = input()
    on = input()
    count = 0
    for i in range(len(on)-1):
        if on[i:i+len(pattern)] == pattern:
            count += 1
    print(f'#{T} {count}')

