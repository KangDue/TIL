"""
1이상 100000이하의 로프가 있다.
각 로프는 들 수 있는 물체의 중량이 서로 다르지만
여러개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌수 있다 .
k개의 로프에 w무게의 물체를 들어올리면 각 로프는 w/k 만큼 무게를 받는다.
모든 로프를 사용할 필요는 없는데 주어진 로프들을 사용해서 들 수 있는 최대 무게는 ?

<접근>
1. 일단 크기 오름차순 정렬
2. 정렬 후 max값 비교 갱신

- 다른 빠른 사람들은
정렬없이 dict로 넣고 (1~10000)
크기 역순조회하며 w/k * k 를 계산해가며 갱신.
"""
o = open('input.txt')
n = int(next(o))
ropes = []
for _ in range(n):
    ropes.append(int(next(o)))
ropes.sort()
maxv = 0
for i in range(n):
    maxv = max(maxv,ropes[i]*(n-i))
print(maxv)