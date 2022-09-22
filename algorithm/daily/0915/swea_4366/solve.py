import sys
sys.stdin = open('input.txt')
"""
은행업무
한 숫자를 2진수랑 3진수로 기억함.
둘다 정확히 1자리씩 잘못 기억하는중.
원래 숫자를 찾아주자!
"""
for t in range(int(input())):
    a = input() #2진수를 스위칭 하면서 3진수와 비교해보자
    b = input() #함수로 비교할게 아니라 3진수도 3씩 달라져야함.
    change = {'0':'12','1':'02','p2':'01'}
    try:
        for i in range(len(a)):
            if a[i] == '1': s = a[:i] + '0' + a[i+1:]
            else: s = a[:i] + '1' + a[i+1:]
            for k in range(len(b)):
                for j in change[b[k]]:
                    th = b[:k]+j+b[k+1:]
                    if int(s,2) == int(th,3):
                        raise Exception
    except:print(f'#{t+1} {int(s,2)}')




