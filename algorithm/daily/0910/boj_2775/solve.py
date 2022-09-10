import sys
sys.stdin = open('input.txt')
# 0층 1호에는 1명이 산다.
# R 층은 0부터 C호는 1부터.
# a 층 b호는 (a-1)층 1~b호까지 사람 총합만큼 살아야한다.
for t in range(int(input())):
    k,n = int(input()),int(input()) #k층 n호
    ans = 0
    temp = range(n + 1)
    for i in range(1,k+1):
        temp2 = [0]
        for j in range(1,n+1):
            temp2.append(temp2[j-1]+temp[j])
        temp = temp2
    print(temp[-1])
#잘보면 조합식이다.
#https://j1w2k3.tistory.com/326 조합식의 변형 참고
# import math
# m = int(input())
# for i in range(m):
#     k = int(input())
#     n = int(input())
#     print(math.comb(n+k,k+1))


