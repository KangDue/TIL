import sys
sys.stdin = open('input.txt')
"""
트리의 순회
in, post가 주어질때 pre 구하기.
post 의 끝은 항상 root 이다. pop 하자.in에서 root를 찾고 좌우로 가른다. (왼족 서브트리, 오른쪽 서브트리)
다시 post에서 pop, in에서 찾고 가른다. (반복)
나타나는 
꼭 다시 풀어보자 
"""
import sys
sys.setrecursionlimit(100000) #재귀 한계 풀어줘야함.
n = int(input())
ino = [*map(int,input().split())]
post = [*map(int,input().split())]
nodes = [0]*(n+1)
for i in range(n): # ino의 item의 위치는 i 라는 뜻
    nodes[ino[i]] = i
tree = [ [] for _ in range(n+1)]
def make_tree(ino_s,ino_e,post_s,post_e,name = ''):
    global tree,ino,post
    if ino_s > ino_e or post_s > post_e: return 0
    root = post[post_e]
    left = nodes[root] - ino_s # 좌측 아이템수
    right = ino_e - nodes[root] # 우측 아이템 수
    print(root,end=" ")
    make_tree(ino_s, ino_s + left - 1, post_s, post_s + left - 1, 'left')  # 왼쪽 서브트리 갱신
    make_tree(ino_e + 1 - right, ino_e, post_e - right, post_e - 1, 'right')  # 오른쪽 서브트리 갱신
make_tree(0,n-1,0,n-1)


#반복문 버전, 고수님들꺼 참고
ans = []
stack = [[0,n-1,0,n-1]]
rpos = {ino[i]:i for i in range(n)} #inorder 배열상 위치 index, 인덱스 + 1 = 개수
while stack:
    ino_s,ino_e,post_s,post_e = stack.pop() #기본구조는 재귀랑 같음. 형태만 재귀 vs 반복문 일 뿐
    root=post[post_e]
    ans.append(root)
    # index - index 는 그 사이의 개수
    left = rpos[root] - ino_s # ino의 시작위치 ~ 자기 자신 위치 제외한 아이템 수
    right = ino_e - rpos[root] # 자기자신 다음 위치부터 ino_e 까지 포함하는 아이템 수.
    if 0 <= rpos[root] < ino_e:
        stack.append([ino_e+1-right,ino_e, post_e - right, post_e - 1])
    if 0<= ino_s < rpos[root]:
        stack.append([ino_s, ino_s + left - 1, post_s, post_s + left - 1])
print(*ans,sep='\n')