import sys
sys.stdin = open('input.txt')
"""
N-queen
변수의 범위 항상 잘 고민하자 ...
"""
def check(r = 0):
    global ans
    if r == n:
        ans += 1
        return 0
    else:
        for i in range(n):
            line[r] = i
            if place(r):
                check(r+1)

#위에서부터 i번째 줄에 j열에 퀸을 놓을때 line[x] = j
def place(x):
    for i in range(x):
        if line[x] == line[i] or abs(line[x]-line[i]) == abs(x-i):
            return 0
    return 1
n = int(input())
line = [0]*n
ans=0
check()
print(ans)


##오류 발생 함수, grid를 dict로 만들고 global로 받아옴,
# def check(r = 0):
#     global grid,ans
#     if r == n: ans += 1; return 0
#     for i in range(n):
#         if not grid[(r,i)]:
#             attack(r,i)
#             check(r+1)
#             attack(r,i,0)
#
# def attack(r,c,val=1):
#     global grid #글로벌로 받아와서 해버리니까 자꾸 원래 공격으로 차있을 공간이 지워져버림
#     for i in range(r,n):
#         if c-(i-r) >= 0: grid[i][c-(i-r)] = val
#         if c+(i-r) < n: grid[i][c+(i-r)] = val
#         grid[i][c] = val
