import sys
sys.stdin = open('input.txt')
#벌집 최소거리 구하기
# 1
# 2,3,4,5,6,7 = 6개
# 8~19 = 12개
# 1에서 다른 벌집까지 가는 최소거리 = 1위치 포함
n = int(input())
layer = [[1,1]]
i = 1
while 1:
    if n <= layer[-1][1]:
        print(i)
        break
    layer.append([ layer[i-1][-1]+1, layer[i-1][-1]+6*i ])
    i += 1
#굳이 시작,끝값 할필요 없이 끝값만 봐도 됨. 그러면 시간 단축