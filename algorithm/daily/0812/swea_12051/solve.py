import sys
sys.stdin = open('input.txt')
T = int(input())
"""
프리셀 게임 언제나 win/lose 뿐
tot = G, today = D 판 했음. Pg %, Pd %
아무것도 모르는데 아는건 오늘 적어도 N판 했다. (D를 정확히 모름)
이게 말이되면 possible, 안되면 broken
"""
for t in range(1,T+1):
    n, pd, pg = map(int, input().split())
    #오늘 승률이 1%인데 게임승수가 1이려면 100판
    #반올림이 아니라 정확한 %이므로 판수가 100의 약수이다.

    #pd * d % 100 = 0 이어야 반올림 안한 승률이 뜬다.
    possibility = []
    for i in range(n,0,-1):
        if (pd*i) % 100: #판수가 안나눠 떨어지면 필요 x
            pass
        else:
            possibility.append(i) #가능한 오늘의 판수 n 추출
            break
    #확실하진 않으나 posi에 전부 추가해버리 runtime에러가 뜨고 추가부분 지우니 시간초과뜸
    #10**15승개까지 주어지다 보니 다넣어버려서 에러뜬거였음. 필요한건 하나라도 있으면 되는거니까 1개만 얻으면 break
    if pg == 100: #
        if pd == 100:
            print(f'#{t} Possible')
        else:
            print(f'#{t} Broken')
    elif pg == 0:
        if pd > 0:
            print(f'#{t} Broken')
        else:
            print(f'#{t} Possible')
    elif not possibility:
        print(f'#{t} Broken')
    else:
        # 10 10 100 일떄
        print(f'#{t} Possible')

    #어제까지 판수 befo_tot, 오늘 판수는 i, #오늘 승수는 i*pd
    #어제까지 승수 x
    #오늘 전체 승률 (x + i*pd)/(befo_tot + i) i가 아무리 커봣자 걍 상수
    #x랑 befo_tot 이 미지수ㅏ 그냥 다 됨


"""
에러 계속 못찾아서 참고한 코드, 결국 스스로 찾음..
황라쿠니 - 수학잘하는 분 같은데
from math import gcd
T = int(input())
for t in range(1, T+1):
    N, PD, PG = map(int, input().split())
    ans = 'Possible'   
    if PD != 100 and PG == 100: ans = 'Broken'
    if PD != 0 and PG == 0: ans = 'Broken'
     
    g = gcd(PD, 100)
    if N < 100 and N < 100//g: ans = 'Broken'
     
    print('#{}'.format(t), ans)
"""