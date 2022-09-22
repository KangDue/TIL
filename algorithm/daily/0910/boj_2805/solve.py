import sys
sys.stdin = open('input.txt')
"""
나무자르기
1. 절단기에 높이 H 지정하면 높이 H상에서 모든나무 절단
p2. 설정가능한 높이는 0또는 양의정수
3. 자른 부분만 들고가고 자르고 남은건 안들고감.
4. 자른 나무의 합이 적어도 M 미터만 되면 끝.
5. 이때 나무 높이의 최댓값을 구하는 프로그램 작성.
"""
n,m = map(int,input().split())
trees = [*map(int,input().split())]
def remain(x,h):
    return x-h if x >= h else 0
#바로 bisection 갈기자!
down = 0
up = max(trees)
while up - down > 1:
    mid = (down+up)//2
    temp = sum(map(lambda x: remain(x,mid),trees))
    if temp < m:# 높이가 딸리면 하향조정
        up = mid
    elif temp > m:
        down = mid
    else:
        print(mid)
        break
else:
    if sum(map(lambda x: remain(x,up),trees)) >= m:
        print(up)
    else:
        print(down)
