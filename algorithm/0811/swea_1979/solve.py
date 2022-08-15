import sys
sys.stdin = open('input.txt')

def check(a, m):
    new = ""
    for i in a:
        new += str(i)
    new = new.split("0") #0기준으로 스플릿
    new = [len(j) for j in new] #연속인 1의 길이를 저장
    return new.count(m) # 카운트

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(T):
    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for i in range(n)]
    tot = 0
    for j in mat:
        tot += check(j, m)
    for k in zip(*mat):
        tot += check(k, m)
    print("#", i + 1, " ", tot, sep="")