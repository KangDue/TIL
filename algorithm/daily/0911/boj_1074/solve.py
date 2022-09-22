import sys
sys.stdin = open('input.txt')
#규칙성을 찾는게 훨 쉬워보이긴 하나
#자꾸 sample은 맞는데 왜틀리나 했더니
#z움직임이 분할한 구역 내에서도 2x2 z순회를 반복 하는 거였다.장난치나?
#인줄 알았더니 z분할하고 그 내부를 z분할하고 그 내부를 z 분할 하는 거였다.
#문제를 정확하게 이해해야한다. 대충 읽고 넘기지말자 ㅠ
# n,r,c = map(int,input().split())
# def zmove(n,r,c):
#     if n == 0: #n=1일땐 최종 2x2 z내부에서 방문순서임.
#         return 0
#     side = p2 ** (n - 1)  # 한 구역의 한 변의 길이
#     area = side * side  # 4구역 중 1 구역 칸 개수
#     r1, r2 = divmod(r, side)  # 몫 기준구역 시작점
#     c1, c2 = divmod(c, side)  # 나머지 기준구역 시작점 기준 현 위치
#     s1 = area * (p2 * r1 + c1)  # 기준 구역 시작점 값.
#     return s1 + zmove(n-1,r2,c2)
# print(zmove(n,r,c))

#짧게 줄여보자
def z(n,r,c):
    if n == 0:return 0
    s=2**(n-1);a=s*s;r1,r2=divmod(r,s);c1,c2=divmod(c,s);return a*(2*r1+c1)+z(n-1,r2,c2)
print(z(*map(int,input().split())))

#백준 숏코딩 1등
# n,r,c=[int(f'{int(z):b}',4)for z in input().split()];print(r*p2+c)