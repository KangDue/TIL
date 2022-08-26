import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
사각형 2개가 주어질떄 겹치는지 판단하기
"""
if __name__ == "__main__":
    import sys
    sr = sys.stdin.readline
    for t in range(4):
        x1, y1, x2 ,y2, x3, y3, x4, y4 = map(int,sr().split())
        c1, w1, h1 = ((x1 + x2) / 2, (y1 + y2) / 2), (x2 - x1) / 2, (y2 - y1) / 2
        c2, w2, h2 = ((x3 + x4) / 2, (y3 + y4) / 2), (x4 - x3) / 2, (y4 - y3) / 2
        ans = ''
        if abs(c2[0]-c1[0]) < w1+w2 and abs(c2[1]-c1[1]) < h1+h2:#직사각형
            ans = 'a'
        elif abs(c2[0]-c1[0]) == w1+w2 and abs(c2[1]-c1[1]) < h1+h2: #선분 옆면 접촉
            ans = 'b'
        elif abs(c2[0]-c1[0]) < w1+w2 and abs(c2[1] - c1[1]) == h1 + h2: #선분 위아래 접촉
            ans = 'b'
        elif abs(c2[0] - c1[0]) == w1 + w2 and abs(c2[1] - c1[1]) == h1 + h2:  # 점 접촉
            ans = 'c'
        else: #안만남
            ans = 'd'
        print(ans)