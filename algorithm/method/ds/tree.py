class Tree:
    def __init__(self,value,parent=None,left=None,right=None,level=0):
        self.parent = parent
        self.value = value
        self.left = left
        self.right = right
        self.level = self.parent.level if self.parent else level
a=Tree('A')
items = []
for i in range(13):
    items.append(Tree(chr(65+i)))
items[0].left = items[1];items[1].parent = items[0]
items[0].right = items[2];items[2].parent = items[0]
items[1].left = items[3];items[3].parent = items[1]
items[1].right = items[4];items[4].parent = items[1]
items[2].left = items[5];items[5].parent = items[2]
items[2].right = items[6];items[6].parent = items[2]
items[3].left = items[7];items[7].parent = items[3]
items[3].right = items[8];items[8].parent = items[3]
items[4].left = items[9];items[9].parent = items[4]
items[5].right = items[10];items[10].parent = items[5]
items[6].left = items[11];items[11].parent = items[6]
items[6].right = items[12];items[12].parent = items[6]

#기본적으로 dfs
#자기자신, 왼쪽, 오른쪽 자식노드 순으로 확인.
def preorder(x):
    print(x.value) #자기부터 보기
    if x.left: #왼쪽 쭉 탐사
        preorder(x.left)
    if x.right: #오른쪽 쭉 탐사
        preorder(x.right)
# preorder(items[0])

def inorder(x):
    if x.left: #왼쪽 쭉 탐사
        inorder(x.left)
    print(x.value) #자신 출력 (왼쪽 자식을 이미 봤거나, 없을때 자기자신 출력)
    if x.right: #오른쪽 쭉 탐사
        inorder(x.right)
# inorder(items[0])

#자식부터보고 자기는 마지막
def postorder(x):
    if x.left: #왼쪽 쭉 탐사
        postorder(x.left)
    if x.right: #오른쪽 쭉 탐사
        postorder(x.right)
    print(x.value) #자신 출력 (왼쪽 자식, 오른쪽 자식 둘다 없을때(이미 봤을때) 자기를 출력)
# postorder(items[0])

n = 13
inputs = [*map(int,'1 p2 1 3 p2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'.split())]
tree = [[0,0] for i in range(n+1)]
for i in range(0,len(inputs),2):
    if tree[inputs[i]][0]:
        tree[inputs[i]][1] = inputs[i+1]
    else: tree[inputs[i]][0] = inputs[i+1]
root = 1
def preorder(x):
    global tree
    print(x) #자기부터 보기
    if tree[x][0]: #왼쪽 쭉 탐사
        preorder(tree[x][0])
    if tree[x][1]: #오른쪽 쭉 탐사
        preorder(tree[x][1])
preorder(root)