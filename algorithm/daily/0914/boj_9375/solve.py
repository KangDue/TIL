import sys
sys.stdin = open('input.txt')
"""
해빈이는 날이 바뀔때마다 한 번 입었던 조합은 절대 다시입지않는다. 뭐라도 추가해야함.
여러 의상들이 주어질때 해빈이는 몇일동안 알몸이 아닌채로 밖에 나갈 수 있을까?
"""
from collections import defaultdict as dd
from functools import reduce
o=open('input.txt');next(o)
o,c=[*map(lambda x:x.split(),o)]+[[0]],dd(int)
for idx in range(1,len(o)):
    if len(o[idx])==1:print(reduce(lambda x, y: x * (y+1), c.values(),1)-1);c = dd(int)
    else:c[o[idx][1]]+=1

#key: 옷의 조합은 각 종류별 옷의 개수 + 1(안입는 경우) 의 곱 - 1(알몸)이다.
#옷을 입는 조합으로만 구하면 불필요한 연산이 너무 많아져서 시간 초과 걸림...

# for t in range(int(next(o)):
#     n = int(input())
#     closet = defaultdict(int)
#     for i in range(n): #의상 안겹침
#         name, kind = input().split()
#         closet[kind]+=1
#     print(sum(map(lambda i:sum(map(lambda a:reduce(lambda x,y:x*y,a),cb(closet.values(),i))),range(1,len(closet)+1))))