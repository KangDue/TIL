import sys
# sys.stdin = open('input.txt')
"""
내려가기
첫행부터 내려가는데 바로아랫 또는 바로 아래 수 이웃으로만 이동 가능
최대 최소 점수를 구하시오!
메모리초과가 떳다.?
한줄씩 받아서 dp 수행하는게 나을듯
테이블을 만드니 메모리 초과뜸
"""
# 입력 그냥 input에서 open으로 바꾸니 50ms 정도 시간 단축
# 이상하게 python3이 압도적으로 시간 많이 잡아먹음
# pypy 204, python3 4508 [ms]
o = open('input.txt')

n = int(next(o))
minr = [0,0,0]
maxr = [0,0,0]
for _ in range(n):
    a,b,c = map(int,next(o).split())
    minr = [a+min(minr[:2]),b+min(minr),c+min(minr[1:])]
    maxr = [a+max(maxr[:2]),b+max(maxr),c+max(maxr[1:])]
print(max(maxr),min(minr))




# nums = [[0]*(5)]+[[0]+[*map(int,input().split())]+[0] for _ in range(n)]
# mindp = [[0]*(5)]+[[10]*(5) for _ in range(n)]
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         mindp[i][j] = nums[i][j] + min(mindp[i-1][j-1:j+2])
# maxdp = [[0]*(5) for _ in range(n+1)]
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         maxdp[i][j] = nums[i][j] + max(maxdp[i-1][j-1:j+2])
#
# print(max(maxdp[-1][1:]),min(mindp[-1][1:]))