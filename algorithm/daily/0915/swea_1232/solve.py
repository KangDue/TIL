import sys
sys.stdin = open('input.txt')


#두 자식노드값을가지고 연산을 수행하니 후위순회하면됨.
oper = {'*':lambda x,y:x*y,'+':lambda x,y:x+y,'-':lambda x,y:x-y,'/':lambda x,y:x//y}
# def post(x):
#     if x>n:return 0
#     post(p2*x)
#     post(p2*x+1)
#     if type(tree[x])==int:return 0
#     else:
#         if p2*x+1 < n+1 and type(tree[p2*x]) == int and type(tree[p2*x+1]) == int:
#             print(tree[x], tree[p2*x],tree[p2*x+1])
#             print(*tree)
#             tree[x] = oper[tree[x]](tree[p2*x],tree[p2*x+1])
#         return 0
#
# for t in range(10):
#     n = int(input())
#     tree = [0] * (n+1)
#     for _ in range(n):
#         a,*b = input().split()
#         if b[0].isdigit():b[0]=int(b[0])
#         tree[int(a)] = b[0]
#     post(1)
#     print(tree[1])

#
oper = {'*':lambda x,y:x*y,'+':lambda x,y:x+y,'-':lambda x,y:x-y,'/':lambda x,y:x//y}
for t in range(10):
    n = int(input())
    ops = []
    vals = [0]*(n+1)
    for _ in range(n):
        a = input().split();a[0]=int(a[0])
        if a[1].isdigit():a[1]=int(a[1]);vals[a[0]]=a[1]
        else:
            a[2]=int(a[2]);a[3]=int(a[3])
            ops.append(a)
    while ops:
        i,v,a,b=ops.pop()
        vals[i]=oper[v](vals[a],vals[b])
    print(f'#{t+1} {vals[1]}')