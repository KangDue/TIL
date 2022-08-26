import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
줄 세우기
"""
if __name__ == "__main__":
    import sys
    sr = sys.stdin.readline
    n = int(sr())
    st = [*map(int,sr().split())]
    real = [1]
    for i in range(1,n): #번호 위치랑 바꾸는게 아니라 번호 앞으로 가는것,첫학생은 걍 1등
        real = real[:i-st[i]]+[i+1]+real[i-st[i]:]
    print(*real)




