import sys
sys.stdin = open('input.txt', encoding='utf-8')

from itertools import combinations
ans =[]
for t in range(1, int(input())+1):
    n, m = map(int,input().split())
    graph = {i:[] for i in range(1,n+1)}
    for _ in range(m):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    count = 0
    for i in range(1,n+1):
        lg = len(graph[i])
        if lg > 1: #적어도 2개점과 연결되어야함
            for a,b in combinations(graph[i],2): #2놈들 조합중
                if a in graph[b]: # 연결되었으면
                    count += 1 #추가
    ans.append(f'#{t} {count//3}') # 3배의 불필요한 연산이 발생하긴 하나 . 그냥 ㄱ
print(*ans,sep = '\n')

# count = 0
# for i in range(m-p2):
#     for j in range(i+1,m-1):
#         for k in range(j+1,m):
#             if len(list(set(info[i] + info[j] + info[k]))) == 3:
#                 count += 1