import sys
sys.stdin = open('input.txt')
"""
숫자만들기
게임으로 사칙연산 공부중 +-*/ 를
숫자들 사이에 끼워넣어 (놓인 순서대로 계산, 연산 우선순위 무시)
최대가 되는 수식과 최소가 되는 수식. 그 차를 구하시오
연산자의 개수는 정해짐. (총 숫자는 들어갈 수 있는 연산자 수와 같다.)
DFS 인듯?
"""
#                cal(r + 1, int(res / nums[r + 1]),text+f'{op[i]} {nums[r+1]}---')#소수점 버림 , 확인용 코드
# op = {0:'+',1:'-',2:'*',3:'/'}
INF = int(1e9)

def cal(r,res):
    global maxv,minv
    if r == n-1:#연산 끝
        minv = min(minv,res)
        maxv = max(maxv,res)
        return 0
    for i in range(4):
        if ops[i]:
            ops[i] -= 1
            if i == 0:
                cal(r+1,(res+nums[r+1]))
            elif i == 1:
                cal(r + 1, (res - nums[r + 1]))
            elif i == 2:
                cal(r + 1, (res * nums[r + 1]))
            elif i == 3:
                cal(r + 1, int(res / nums[r + 1]))#소수점 버림
            ops[i] += 1
        else:
            continue

for t in range(int(input())):
    n = int(input())
    ops = [*map(int,input().split())]
    nums = [*map(int,input().split())]
    INF = int(1e9+1)
    maxv,minv = -INF,INF
    cal(0,nums[0])
    print(f'#{t+1} {maxv-minv}')
