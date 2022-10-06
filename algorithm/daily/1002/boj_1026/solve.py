"""
정수 배열 A,B가 있을때
두 배열의 같은 위치의 원소들 끼리 곱한 값의 합 = S
이를 최소화 하기 위한 A의 수를 재배열 하자.
S의 최솟값을 출력하는 프로그램을 만들자!

A,B의 최대 길이는 50이다.
각 원소는 0 이상 100 이하의 정수이다.

각각을 카운팅 소트를 통해 누적합 순위를 구하고
그 순위의 맞는 값들을 서로 매칭시켜 곱한다.
B의 값이 클수록 A의 작은 값을 곱한다.
A를 재배열, B는 재배열 하지 말라하지만
하나를 재배열 하는건 결국 둘 다 재배열 하는  것과 같은 결과임.

두 배열을 카운팅 정렬을 하나는 오름차순, 하나는 내림차순으로 하면
두 배열의 곱이 최소가 된다.

-백준 시간 1등 코드는 A를 sort후 B를 max값만 뽑으면서 하나씩 pop함.ㅠ;
"""
o = open('input.txt')
n = int(next(o))
A = [0]*101
for i in map(int,next(o).split()):
    A[i] += 1

B = [0]*101
for i in map(int,next(o).split()):
    B[i] += 1
ra,rb = [],[]

for i in range(101):
    if A[i]:
        ra += [i]*A[i]
    if B[100-i]:
        rb += [100-i]*B[100-i]

ans = 0
for i in range(n):
    ans += ra[i]*rb[i]
print(ans)