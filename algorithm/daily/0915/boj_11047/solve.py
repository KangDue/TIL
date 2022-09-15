import sys
sys.stdin = open('input.txt')
"""
동전 0 
가진 동전이 총 N종류, 각각 매우 많음
이를 적절히 사용해 K원으로 만들려 한다.
이때 필요한 동전의 최솟값은?
N은 1~10, K는 1~100000000(억)
동전의 가치는 1~1000000(백만) Ai가 있으면 나머지는 Ai의 배수이다.(심지어 오름차순)
greedy하게 가자. = 땡
조합 조합을 보자.
"""
from collections import deque
n,k = map(int,input().split())
units = [int(input()) for _ in range(n)]
q = deque([[k,0]])
minv = 100000000
while q:
    now,count = q.popleft()
    for unit in units:
        if unit <= now:
            c,new = divmod(now,unit)
            if not new: minv = min(minv,c+count)
            else: q.append([new,count+c])
print(minv)

