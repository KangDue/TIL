#유니온 파인드(disjoint_set)
"""
집합을 관리하는 자료구조로서
아래 2가지 연산이 가능하다
1) 요소 A가 요소 B와 같은 집합에 속하는지 확인
p2) 요소 A가 속한 집합 A와 요소 B가 속한 집합을 병합

파이썬의 자료형 set을 그대로 쓰는것과는 느낌이 다름. tree와 비슷
"""
class ds:
    def __init__(self,value= None , parent = None):
        self.value = value
        self.child = set() #ds오브젝트로 값을 저장하기에 value는 중복될 수 있다.
        self.parent = None
    def add(self,other):
        if isinstance(other,list):
            self.child.update(other)
            for i in other:
                i.parent = self
        else:
            self.child.add(other)
            other.parent = self
    @property
    def find_p(self):
        me = self
        c = 0
        while me.parent:
            me = me.parent
            c += 1
        return me,c
def merge(x,y):
    a, ac = x.find_p
    b, bc = y.find_p
    if ac < bc:
        b.parent = a
    else:
        a.parent = b

a = ds(3)
b = ds(1)
c = ds(2)
a.add([b,c])
d = ds(4)
e = ds(5)
d.add(e)
print(a.child)
print(b.parent.value)
print(b.find_p[0].value) # find_p 작동 확인
merge(e,c)
print(e.find_p[0].value) # 정상적으로 병합 작동 확인