import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
경비원 
사각형 지도에서 무조건 변을따라 이동해야 한다.
처음 위치에서 시계 또는 반시계방향 이동에 따라 거리가 달라짐
동근이의 위치와 각 상점 사이 최단 거리의 합 구하기.
북,남,서,동 = 1 2 3 4 블록 기준 상점들 위치
상점과 동근이 위치는 꼭짓점이 될 수 없다.
"""
if __name__ == "__main__":
    import sys
    sr = sys.stdin.readline
    w,h = map(int,sr().split())
    store = [map(int,sr().split()) for i in range(int(sr()))]
    dp,dd = map(int,sr().split())
    ans = 0
    for x,y in store:
        if dp == 1:
            if x == 1:
                ans += abs(dd-y)
            elif x == 2:
                ans += min(dd+y,2*w-dd-y) + h
            elif x == 3:
                ans += dd + y
            elif x == 4:
                ans += (w - dd)+y
        elif dp == 2:
            if x == 1:
                ans += min(dd + y, 2 * w - dd - y) + h
            elif x == 2:
                ans += abs(dd - y)
            elif x == 3:
                ans += dd + (h - y)
            elif x == 4:
                ans += (w - dd) + (h - y)
        elif dp == 3:
            if x == 1:
                ans += dd + y
            elif x == 2:
                ans += (h - dd) + y
            elif x == 3:
                ans += abs(dd - y)
            elif x == 4:
                ans += min(dd + y, 2 * h - dd - y) + w
        elif dp == 4:
            if x == 1:
                ans += dd + (w - y)
            elif x == 2:
                ans += (h - dd) + (w - y)
            elif x == 3:
                ans += min(dd + y, 2 * h - dd - y) + w
            elif x == 4:
                ans += abs(dd-y)
    print(ans)
