import sys
sys.stdin = open('input.txt')
#복 습 필 수!
"""
색종이 영역 구하기
붙이는 종이는 가로세로 10, 변은 도화지의 가로 세로와 평행
색종이의 왼쪽 아래 모서리 위치가 주어짐.
"""
# if __name__ == "__main__":
#     import sys
#     sr = sys.stdin.readline
#     n = int(sr())
#     #간단하게 칠하자 ^^
#     xx = []
#     yy = []
#     for i in range(n):
#         x,y = map(int,sr().split())
#         xx.append(x)
#         yy.append(y)
#     mx = max(xx)
#     my = max(yy)
#     grid = [[0 for _ in range(mx+11)] for _ in range(my+11)]
#     for z in range(n):
#         for i in range(yy[z],yy[z]+10):
#             for j in range(xx[z],xx[z]+10):
#                 grid[i][j] = 1
#     ans = 0
#     for i in range(my+11):
#         for j in range(mx+11):
#             if grid[i][j] == 1:
#                 ans += 1
#     print( ans )

#신기한 숏코딩 해석
t=range(10)
print(len({(a+x,b+y)for a,b in eval('map(int,input().split()),'*int(input())) for x in t for y in t}))

fill = set()
for a,b in eval('map(int,input().split()),'*int(input())):
    for x in range(10):
        for y in range(10):
            fill.add((a + x, b + y))
print(len(fill))