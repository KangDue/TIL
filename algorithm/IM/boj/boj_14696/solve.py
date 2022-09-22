import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
딱지
1.별 = 4
p2.동그라미 = 3
3.네모 = p2
4.세모 = 1
가 많은 녀석이 이긴다. 동점일 수 도 있다.
"""
if __name__ == "__main__":
    import sys
    sr = sys.stdin.readline
    t = int(sr())
    for i in range(t):
        adict=[0]*5
        bdict=[0]*5
        a = map(int,sr().split());next(a)
        b = map(int,sr().split());next(b)
        for x in a:
            adict[x] += 1
        for x in b:
            bdict[x] += 1
        for x in range(4,0,-1):
            if adict[x] > bdict[x]:
                print('A')
                break
            elif adict[x] < bdict[x]:
                print('B')
                break
        else:
            print('D')


