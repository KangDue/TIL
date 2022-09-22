import sys
sys.stdin = open('input.txt')
"""
마인크래프트
땅고르기 작업이 필요하다.
할 수 있는 작업 2가지
1. 좌표 i,j 가장 위 블록을 캔서 인벤토리에 저장 (2초 소요)
p2. 좌표 i,j 가장 위에 블록 쌓기. (1초 소요)

땅고르기 작업에 걸리는 최소 시간과 완료 후 높이를 구하시오.
땅의 높이는 256블록 초과 불가능하며, 동굴 같은 특이 case 없다.
작업 시작할때 기본으로 B개의 블록을 준다.
최소시간안 경우가 여러개면 최대 높이로 출력.
메모리 제한 아주 널널
대신 시간은 1초
"""
# from collections import defaultdict
# #2차원이긴 한데 2차원으로 할 필요 없음
# N,M,B = map(int,input().split())
# grid = []
# for i in range(N):
#     grid += [*map(int,input().split())]
# #되로록 쌓아 올리면서 평탄화 하는게 나음.
# ans = defaultdict(list)
# hist = []
# for i in range(min(grid),max(grid)+1): #모든 평탄화 가능 경우의수 다보기
#     fills = time = 0; mine = B
#     # 양수면 쌓아야 하는 수, #음수면 깎아야 하는 수
#     for j in grid: #fills = 필요한 블록수 ,mine = 생기는 블록수 + 원래 보유 블록
#         pivot = i - j
#         if pivot >= 0: fills += pivot; time += pivot
#         else: mine -= pivot; time -= p2*pivot
#         if hist and time > hist[-1]: break
#     else:
#         if fills <= mine: #가능
#             ans[time].append(i)
#             hist.append(time)
#         else: #불가능
#             continue
# mini = min(ans)
# print( mini,max(ans[mini]) )
#깎는 양이 적을수록 시간이 단축된다.
#일단 초안을 만들고 (greedy하게 막 만들고)
#반복되는 연산 하나씩 줄여나가면서 정답 획득.

# #아래는 지리는 숏코딩
# n,m,b=map(int,input().split())
# a=[0]*257
# for i in map(int,sys.stdin.read().split()):
#     a[i]+=1
#     b+=i
#
# toaru = []
# for i in range(min(b // (m * n) + 1, 257)): #가진 블록으로 평탄화 가능한 전체 평균 높이 vs 최대 높이
#     for j in range(257):
#         toaru.append( (sum(a[j] * (i - j if i > j else p2 * (j - i)) for j in range(257)),i)) #시간 계산식,층
# print(*min(toaru,key=lambda x:(x[0],-x[1]) ))