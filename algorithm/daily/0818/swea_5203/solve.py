import sys
sys.stdin = open('input.txt', encoding='utf-8')

def rcheck(x):
    for i in range(10-2): # 범위 -에서 -2로 수정후 tc 8개에서 9개 맞는걸로 바뀜
        if x[i] and x[i+1] and x[i+2]:
            x[i] -= 1; x[i+1] -= 1; x[i+2] -= 1
            return True
    else:
        return False
def tcheck(x):
    if 3 in x:
        x[x.index(3)] -= 3
        return True
    else:
        return False

for t in range(1,int(input()) +1 ): # 공평하게 카드수가 같을때 비교하는게 아니라, 진짜 먼저 뽑으면 이김. p1 이 유리한 게임.;; 이거 때매 계속 틀렸네
    cards = list(map(int,input().split()))#텍스트로 처리해도 되는데 정수가 편함
    p1, p2 = [0]*10, [0]*10
    draw = False
    s1, s2 = 0, 0
    for i in range(6):
        p1[cards[2*i]] += 1
        s1 += rcheck(p1) + tcheck(p1)  # r또는 p가 중복되면 안먹혀서 수정해야함
        if s1 > s2:
            print(f'#{t} 1');break
        elif s1 < s2:
            print(f'#{t} 2');break
        p2[cards[2*i+1]] += 1
        s2 += rcheck(p2) + tcheck(p2)
        if s1 > s2:
            print(f'#{t} 1');break
        elif s1 < s2:
            print(f'#{t} 2');break
    else:#무사히 반복 종료시
        print(f'#{t} 0')


