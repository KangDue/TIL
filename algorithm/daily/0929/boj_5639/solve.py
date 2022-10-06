import sys
sys.stdin = open('input.txt')
"""
이진검색트리를 전위순회한 결과가 주어질 때,
이 트리를 후위 순회한 결과를 출력하시오
노드 값은 모두 양의 정수
내꺼는 트리르 만들고 새로 후위순회를 하는거라 pypy로는 통과인데
python3는 시간초과
"""
import sys
sys.setrecursionlimit(10000) #노드 1000개까지 주어지니까 최악의 경우 대비 깊이 늘려줘야함.
class Tree:
    def __init__(self,value,left=None,right=None):
        self.left = left
        self.right = right
        self.value = value
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return str(self.value)
    def __gt__(self,other):
        return self.value > other.value
    def __lt__(self, other):
        return self.value < other.value

pre = [*map(lambda x:Tree(int(x)),open('input.txt'))]
root = pre[0]
for i in range(1,len(pre)):
    temp = root
    while temp:
        if pre[i] > temp and temp.right: # root보다 큰데 이미 오른쪽 자식이 있다면
            temp = temp.right
            continue
        elif pre[i] < temp and temp.left:
            temp = temp.left
            continue
        elif pre[i] > temp: #자리 비었으면 채운다.
            temp.right = pre[i]
            break
        elif pre[i] < temp: #자리 비었으면 채운다.
            temp.left = pre[i]
            break

def post(x):
    if x.left:
        post(x.left)
    if x.right:
        post(x.right)
    print(x)

post(root)

## 속도 빠른거 참고.
import sys
def dfs(pos, min_v): #이렇게 받은 list에서 바로 post 오더로 출력.
    ret = 0
    if pos + 1 < len(orders) and orders[pos] > orders[pos + 1]:
        ret += dfs(pos + 1, min(min_v, orders[pos]))
    if pos + ret + 1 < len(orders) and orders[pos] < orders[pos + ret + 1] \
        and orders[pos + ret + 1] < min_v:
        ret += dfs(pos + ret + 1, min_v)
    print(orders[pos])
    return ret + 1

sys.setrecursionlimit(10009)

orders = []
for v in map(int, sys.stdin.read().split()):
    orders.append(v)
dfs(0, 0x3c3c3c3c)