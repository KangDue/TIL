import sys
sys.stdin = open('input.txt')
"""
트리 순회
입력받아 ,전위, 중위 ,후위 순회한 결과 출력

## 실수
- 처음에 .이면 y를 제외하고 z만 어펜드 하고 0,1인덱스를 사용하니
- 왼쪽/ 오른쪽 구분을 못해서 무조건 2개넣고 해결
"""
from collections import defaultdict
n = int(input())
# node = {chr(65+i):i+1 for i in range(26)}
tree = defaultdict(list)
for _ in range(n):
    x,y,z = input().split()
    tree[x].append(y)
    tree[x].append(z)
pre_ans = ''
ino_ans = ''
post_ans = ''
def pre(x):
    global pre_ans
    pre_ans += x
    try:pre(tree[x][0])
    except:pass
    try:pre(tree[x][1])
    except:pass

def ino(x):
    global ino_ans
    try:ino(tree[x][0])
    except:pass
    ino_ans += x
    try:ino(tree[x][1])
    except:pass

def post(x):
    global post_ans
    try:post(tree[x][0])
    except:pass
    try:post(tree[x][1])
    except:pass
    post_ans += x

pre('A')
print(pre_ans.replace('.',''))
ino('A')
print(ino_ans.replace('.',''))
post('A')
print(post_ans.replace('.',''))