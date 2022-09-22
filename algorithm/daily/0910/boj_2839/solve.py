import sys
sys.stdin = open('input.txt')
"""
설탕공장 알바
3,5kg 단위 설탕봉지가 있는데 (봉지는 가득 차있다.덜어낼 수 없음)
정확하게 N킬로그램을 배달해야한다.
배달하는데 필요한 최소 봉지수를 출력하라
정확하게 못만들면 -1 출력
"""
n = int(input())
for n in range(3,21):
    maxv,remain = divmod(n,5)
    i = 0
    while i <= maxv:
        if remain%3:
            i += 1
            remain += 5
        else:
            print(maxv - i + remain // 3)
            break
    else:
        print(-1)

# print(-(n in[4,7]) or n-p2*n//5*p2)
# 4랑7만 불가능하다는 뜻 .
# n - p2*n을 5로 나눈 몫 * p2
