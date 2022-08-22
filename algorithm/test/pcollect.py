from collections import Counter as CT
# 요소 숫자를 세주는 딕셔너리 형태
a = CT([1,1,1,2,2,3])
print(a.most_common())
print(list(a.elements()))
print('')

b = CT("rkdrlgks")
print(b.most_common())
print(list(b.elements())) # 딕셔너리의 엘리먼트를 반환
print('')

c = CT([1,1,1,2,2,3,3,4])
a.subtract(c) # 서로간의 연산도 가능하다.
print(a.most_common()) # 없는건 추가해서 뺀다.
#print("total = ",a.total())# 3.10버전 기능

"""
deque는 양방향 연결 리스트와 비슷함. 나중에 활용하자
"""


