import sys
sys.stdin = open('input.txt')


def check(num):
    run, tri = 0, 0
    for i in range(10):  # 트리플렛 찾기
        if num[i] == 3:
            tri += 1
            num[i] -= 3
        elif num[i] == 6:  # 트리플렛 2개
            return 1

    for k in range(10):  # 런 찾기
        if num[k:k + 3] == [1, 1, 1]:
            run += 1
            num[k:k + 3] = [0, 0, 0]
        elif num[k:k + 3] == [2, 2, 2]:  # 런 두개
            return 1

    if tri + run == 2:
        return 1
    else:
        return 0


T = int(input())
for t in range(1,T+1):
    cards = list(map(int,input()))
    num = [0 for i in range(10)]
    # 카운팅 소트 적용하면 편할듯?
    for i in cards:
        num[i] += 1
    print(f'#{t} {check(num)}')
