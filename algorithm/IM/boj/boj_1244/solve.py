import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
1. 남학생은 스위치번호가 자기수의 배수면 모든 배수인 스위치 조작
p2. 여학생은 자기 번호 중심으로 가장 큰 좌우 대칭인 구역의 스위치를 조작(항상 홀수개)
첫줄 스위치는 100이하
둘째둘 스위치 상태 켜지면 1/ 꺼지면0
셋쩨는 학생수(남1 /여2)
"""
if __name__ == "__main__":
    import sys
    sr = sys.stdin.readline
    def sym(x, a=0):
        if x+a <= switch_num and x-a > 0:
            if switch_state[x - a] != switch_state[x + a]:
                for i in range(x - (a - 1), x + a):
                    switch_state[i] ^= 1
            else:
                return sym(x, a + 1)
        else:
            for i in range(x - (a - 1), x + a):
                switch_state[i] ^= 1

    def mul(x):  # 배수만 바꾸기
        for i in range(x, switch_num+1, x):
            switch_state[i] ^= 1

    def act(num, gen):
        if gen == 1: return mul(num)
        else: return sym(num)

    switch_num = int(sr())
    switch_state = [-1] + [*map(int,sr().split())] # 1번부터 시작
    for _ in range(int(sr())):
        gen, num = map(int,sr().split())
        act(num, gen)
    #한줄에 20개씩 출력한다.
    for k in range(1,switch_num+1):
        print(switch_state[k],end=" ")
        x,y = divmod(k, 20)
        if x and y == 0:print()

