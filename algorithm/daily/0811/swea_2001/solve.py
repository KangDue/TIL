import sys
sys.stdin = open('input.txt')

class mat(list):
    def filter_sum(self, a, b, c, d):  # a,b 는 행 index, c,d = 열 index
        temp = mat([])
        for i in range(a, b):
            for k in range(c, d):
                temp.append(self[i][k])
        return sum(temp)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(T):
    n, m = map(int, input().split())
    fly = mat([list(map(int, input().split())) for i in range(n)])

    mats = []
    for k in range(n - m + 1):
        for j in range(n - m + 1):
            mats.append(fly.filter_sum(k, k + m, j, j + m))
    print("#", i + 1, " ", max(mats), sep="")