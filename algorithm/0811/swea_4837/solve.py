import sys
sys.stdin = open('input.txt')

#1~12 자연수로 이루어진 집합A
#이중 원소가 N개 원소의 합이 K인 부분집합 갯수
#없으면 0

#n번째 마지막 값부터 차곡 차곡 123 124 125 순서로.
def ksum(x, n):  # yiled generator 예제보고 활용해보기
    for i in range(len(x)):
        if n == 1:
            yield [x[i]]
        else:
            for element in ksum(x[i + 1:], n - 1):
                yield [x[i]] + element

T = int(input())
for t in range(1,T+1):
    n,k = map(int,input().split())
    count = 0
    limit = k if k < 12 else None #조기종료 조건. 단순하게
    if limit:
        for i in ksum(range(1,13),n):
            if i[0] > k:
                break
            elif sum(i) == k:
                count += 1
        print(f'#{t} {count}')
    else:
        for i in ksum(range(1,13),n):
            if sum(i) == k:
                count += 1
        print(f'#{t} {count}')


















