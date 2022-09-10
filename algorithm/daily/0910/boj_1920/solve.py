import sys
sys.stdin = open('input.txt')

ans = []
temp = dict()
n = int(input())
for i in map(int,input().split()):
    temp.setdefault(i,1)
m = int(input())
for i in map(int,input().split()):
    if temp.get(i):
        ans.append(1)
    else:
        ans.append(0)
print(*ans,sep='\n')

# 이게 왜 더 빠르노 ??? 생성,삭제 구간이 적어서 그런가>?
# z,z,t,t=open('input.txt')
# z={*z.split()}
# for i in t.split():
#     print(+(i in z))