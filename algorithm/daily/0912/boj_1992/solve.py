import sys
sys.stdin = open('input.txt')
"""
흑백영상을 압축표현하는 데이터구조인 쿼드 트리(Quad Tree)가 있다.
흰점 0, 검은점 1
쿼드트리는 같은곳에 같은색이 몰려있으면 이를 압축하여 간단히 표현 가능
모두 한가지 색이 아니면 ()를 일단 씌우고 4구역으로 나눠서 판별한다.
"""
n = int(input())
grid = [input() for _ in range(n)]
test = ''
def check(r,c,n):
    pivot = grid[r][c]
    global test
    for i in range(r,r+n):#지정된 행에서
        if grid[i][c:c+n].count(pivot) != n:
            test += '('
            for y in range(r,r+n,n//2):
                for x in range(c,c+n,n//2):
                    check(y,x,n//2)
            test += ')'
            break
    else:#다 같은 색이면
        test += str(pivot)
check(0,0,n)
print(test)

#깊이별 요소 저장본
# ans = []
# def check(r,c,n,pos):
#     pivot = grid[r][c]
#     global test
#     if n==1:
#         ans.append([pivot,pos])
#     for i in range(r,r+n):#지정된 행에서
#         if grid[i][c:c+n].count(pivot) != n:
#             for y in range(r,r+n,n//p2):
#                 for x in range(c,c+n,n//p2):
#                     check(y,x,n//p2,pos+1)
#             break
#     else:#다 같은 색이면
#         ans.append([pivot,pos])
#         test += str(pivot)