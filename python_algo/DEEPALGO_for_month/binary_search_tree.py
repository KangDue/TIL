a = [5,4,16,7,3,9,1]
class BST:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self): #객체의 정보
        return str(self.value)
    def __repr__(self): #리스트 프린트시 객체 자체 meta 정보
        return str(self.value)

a = [BST(i) for i in a]

def make_tree(x):#중복값은 없다.
    if len(x) == 1:
        return  x[0]
    if not x:
        return None
    pivot = x[len(x)//2]
    left,right = [],[]
    for i in x:
        if i.value < pivot.value:
            left.append(i)
        elif i.value > pivot.value:
            right.append(i)
    pivot.left = make_tree(left)
    pivot.right = make_tree(right)
    return pivot
root = make_tree(a)

def inorder(x):
    if x.left:
        inorder(x.left)
    print(x)
    if x.right:
        inorder(x.right)

inorder(root)

import sys
#길이가 100만일 때
DICT = {i:[] for i in range(1000000)} #dict 는 크기 계산시 value의 크기는 포함 안됨.
LIST = [i for i in range(1000000)]
SET = {i for i in range(1000000)}
GENERATOR = (i for i in range(1000000))
STR = '1'*1000000
#메가바이트
print("DICT",round(sys.getsizeof(DICT)/1024/1024,5))
print("LIST",round(sys.getsizeof(LIST)/1024/1024,5))
print("SET",round(sys.getsizeof(SET)/1024/1024,5))
print("GENERATOR",round(sys.getsizeof(GENERATOR)/1024/1024,5))
print("STR",round(sys.getsizeof(STR)/1024/1024,5))
print("INT",round(sys.getsizeof(1000000)/1024/1024,5))
print("FLOAT",round(sys.getsizeof(1000000.0)/1024/1024,5))
print("c",sys.getsizeof('1'))
print("d",sys.getsizeof(1))
print("f",sys.getsizeof(1.0))
print("dict",sys.getsizeof({1:0,2:0})) #
print("set",sys.getsizeof(set([1,2]))) # 여유 크기를 잡아두고 시작해서 원소 최초 몇개는 저장해도 크기 안변함.
print("list",sys.getsizeof([1,2])) # 원소 하나 추가시가마 8byte 씩 증가


"""
generator가 메모리 아끼끼 확실히 좋다 ㅎ
각각 메모리를 아껴야한다 vs 시간을 아껴야한다 vs 기능이 필요하다 를 고민해서 결정
FLOAT형은 꼭 필요한거 아니면 왠만하면 int형으로 int도 필요없다면 str로 하자.

그리고 하나의 저장 공간에 여러개의 원소가 만들어지는지
원소는 몇개 없는데 저장공간이 여러개인지도 구분해야함. 각자 기본 크기가 다르기 때문
"""

import sys
print(sys.byteorder)