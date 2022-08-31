import sys
sys.stdin = open('input.txt')
#복 습 필 수!


if __name__ == "__main__":
    import sys
    n = int(input())
    #자기가 1등일떄, 2등일때를 min으로 비교하며 더해가자
    #그 이전 계산기록은 필요가 없다.
    fs=fn=0
    a = [*map(int, input().split())]
    st = a.index(min(a))  # 가장 작은값
    nd = n - (a.index(max(a)) + st)  # 중간값 인덱스
    ini = [0,0,0]
    for i in range(n):
        a = [*map(int,input().split())]
        st = a.index(min(a)) #가장 작은값
        nd = n - (a.index(max(a))+st) #중간값 인덱스



